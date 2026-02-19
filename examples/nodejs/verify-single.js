// Verify a single email address using MyEmailVerifier API
// Run: node verify-single.js

require('dotenv').config();
const axios = require('axios');

const API_KEY = process.env.MYEMAILVERIFIER_API_KEY || 'YOUR_API_KEY';

/**
 * Option 1: Fast API (Recommended for AI/Automation)
 */
async function verifyEmailFastAPI(email) {
  try {
    console.log(`Verifying email (Fast API): ${email}`);

    const response = await axios.get('https://api.myemailverifier.com/api/validate_single.php', {
      params: {
        apikey: API_KEY,
        email: email
      },
      timeout: 10000
    });

    const result = response.data;

    // Display results
    console.log('\n=== Verification Result ===');
    console.log(`Email: ${result.Address}`);
    console.log(`Status: ${result.Status}`);
    console.log(`Diagnosis: ${result.Diagnosis}`);
    console.log(`Catch-all: ${result.catch_all}`);
    console.log(`Role-based: ${result.Role_Based}`);
    console.log(`Disposable: ${result.Disposable_Domain}`);
    console.log(`Free Domain: ${result.Free_Domain}`);
    console.log(`Greylisted: ${result.Greylisted}`);

    return result;
  } catch (error) {
    if (error.response) {
      console.error(`Error: HTTP ${error.response.status}`);
      if (error.response.status === 429) {
        console.error('Rate limit exceeded');
      } else if (error.response.status === 401) {
        console.error('Invalid API key');
      }
    } else {
      console.error('Error verifying email:', error.message);
    }
    return null;
  }
}

/**
 * Option 2: Client API (Comprehensive)
 */
async function verifyEmailClientAPI(email) {
  try {
    console.log(`Verifying email (Client API): ${email}`);

    const response = await axios.get(
      `https://client.myemailverifier.com/verifier/validate_single/${email}/${API_KEY}`,
      { timeout: 10000 }
    );

    const result = response.data;

    // Display results (same format)
    console.log('\n=== Verification Result ===');
    console.log(`Email: ${result.Address}`);
    console.log(`Status: ${result.Status}`);
    console.log(`Diagnosis: ${result.Diagnosis}`);

    return result;
  } catch (error) {
    console.error('Error:', error.response?.data || error.message);
    return null;
  }
}

/**
 * Get credit balance
 */
async function getCredits() {
  try {
    const response = await axios.get(
      `https://client.myemailverifier.com/verifier/getcredits/${API_KEY}`
    );
    
    console.log(`Remaining Credits: ${response.data.credits}\n`);
    return response.data.credits;
  } catch (error) {
    console.error('Error getting credits:', error.message);
    return null;
  }
}

// Test with different emails
async function main() {
  // Check credits first
  await getCredits();
  
  const testEmails = [
    'valid@example.com',
    'support@myemailverifier.com'
  ];

  for (const email of testEmails) {
    // Use Fast API (recommended)
    await verifyEmailFastAPI(email);
    
    // Or use Client API
    // await verifyEmailClientAPI(email);
    
    console.log('\n');
  }
}

main();
