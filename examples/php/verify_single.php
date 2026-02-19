<?php
/**
 * Verify a single email address using MyEmailVerifier API
 * Run: php verify_single.php
 */

// Configuration
$apiKey = getenv('MYEMAILVERIFIER_API_KEY') ?: 'YOUR_API_KEY';

/**
 * Option 1: Fast API (Recommended)
 */
function verifyEmailFastAPI($email, $apiKey) {
    echo "Verifying email (Fast API): $email\n";
    
    $url = "https://api.myemailverifier.com/api/validate_single.php?apikey=" . urlencode($apiKey) . "&email=" . urlencode($email);
    
    $ch = curl_init();
    curl_setopt_array($ch, [
        CURLOPT_URL => $url,
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_TIMEOUT => 10,
        CURLOPT_SSL_VERIFYPEER => true
    ]);
    
    $response = curl_exec($ch);
    $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    
    if ($httpCode !== 200) {
        echo "Error: HTTP $httpCode\n";
        if ($httpCode === 429) {
            echo "Rate limit exceeded\n";
        } elseif ($httpCode === 401) {
            echo "Invalid API key\n";
        }
        curl_close($ch);
        return null;
    }
    
    curl_close($ch);
    $result = json_decode($response, true);
    
    // Display results
    echo "\n=== Verification Result ===\n";
    echo "Email: " . ($result['Address'] ?? 'N/A') . "\n";
    echo "Status: " . ($result['Status'] ?? 'N/A') . "\n";
    echo "Diagnosis: " . ($result['Diagnosis'] ?? 'N/A') . "\n";
    echo "Catch-all: " . ($result['catch_all'] ?? 'N/A') . "\n";
    echo "Role-based: " . ($result['Role_Based'] ?? 'N/A') . "\n";
    echo "Disposable: " . ($result['Disposable_Domain'] ?? 'N/A') . "\n";
    echo "Free Domain: " . ($result['Free_Domain'] ?? 'N/A') . "\n";
    echo "Greylisted: " . ($result['Greylisted'] ?? 'N/A') . "\n\n";
    
    return $result;
}

/**
 * Option 2: Client API (Comprehensive)
 */
function verifyEmailClientAPI($email, $apiKey) {
    echo "Verifying email (Client API): $email\n";
    
    $url = "https://client.myemailverifier.com/verifier/validate_single/" . urlencode($email) . "/" . urlencode($apiKey);
    
    $ch = curl_init();
    curl_setopt_array($ch, [
        CURLOPT_URL => $url,
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_TIMEOUT => 10,
        CURLOPT_SSL_VERIFYPEER => true
    ]);
    
    $response = curl_exec($ch);
    $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    curl_close($ch);
    
    if ($httpCode !== 200) {
        echo "Error: HTTP $httpCode\n";
        return null;
    }
    
    $result = json_decode($response, true);
    
    // Display results (same format as Fast API)
    echo "\n=== Verification Result ===\n";
    echo "Email: " . ($result['Address'] ?? 'N/A') . "\n";
    echo "Status: " . ($result['Status'] ?? 'N/A') . "\n";
    echo "Diagnosis: " . ($result['Diagnosis'] ?? 'N/A') . "\n\n";
    
    return $result;
}

/**
 * Get credit balance
 */
function getCredits($apiKey) {
    $url = "https://client.myemailverifier.com/verifier/getcredits/" . urlencode($apiKey);
    
    $ch = curl_init();
    curl_setopt_array($ch, [
        CURLOPT_URL => $url,
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_TIMEOUT => 5
    ]);
    
    $response = curl_exec($ch);
    curl_close($ch);
    
    $result = json_decode($response, true);
    echo "Remaining Credits: " . ($result['credits'] ?? 'N/A') . "\n\n";
    
    return $result;
}

// Main execution
function main() {
    global $apiKey;
    
    // Check credits first
    getCredits($apiKey);
    
    $testEmails = [
        'valid@example.com',
        'support@myemailverifier.com'
    ];
    
    foreach ($testEmails as $email) {
        // Use Fast API (recommended)
        verifyEmailFastAPI($email, $apiKey);
        
        // Or use Client API
        // verifyEmailClientAPI($email, $apiKey);
    }
}

main();
?>