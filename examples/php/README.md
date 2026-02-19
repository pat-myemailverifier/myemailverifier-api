# PHP Examples

Complete examples for using MyEmailVerifier API with PHP.

## Installation

```bash
composer require requests/requests
```

Or use cURL (built-in):
```php
// No installation needed
```

## Basic Usage

See the example files in this directory:

- `verify_single.php` - Verify a single email
- `verify_batch.php` - Verify multiple emails
- `domain_validation.php` - Validate domain
- `error_handling.php` - Handle errors properly

## Quick Start

```php
<?php
$apiKey = 'your_api_key';
$baseUrl = 'https://api.myemailverifier.com';

$data = [
    'email' => 'user@example.com',
    'api_key' => $apiKey
];

$ch = curl_init();
curl_setopt_array($ch, [
    CURLOPT_URL => "$baseUrl/verify",
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_POST => true,
    CURLOPT_POSTFIELDS => json_encode($data),
    CURLOPT_HTTPHEADER => ['Content-Type: application/json']
]);

$response = curl_exec($ch);
curl_close($ch);

$result = json_decode($response, true);
print_r($result);
?>
```

## Configuration

Set environment variables or use .env:
```php
<?php
require 'vendor/autoload.php';
$dotenv = Dotenv\Dotenv::createImmutable(__DIR__);
$dotenv->load();

$apiKey = $_ENV['MYEMAILVERIFIER_API_KEY'];
?>
```

## Running Examples

```bash
# Single email verification
php verify_single.php

# Batch verification
php verify_batch.php

# Domain validation
php domain_validation.php

# Error handling
php error_handling.php
```

## More Information

- [Back to examples](../)
- [API Reference](../../docs/API_REFERENCE.md)
- [Getting Started](../../docs/GETTING_STARTED.md)
