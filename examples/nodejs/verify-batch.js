// Batch verify multiple emails
// Run: node verify-batch.js

require('dotenv').config();
const axios = require('axios');

const API_KEY = process.env.MYEMAILVERIFIER_API_KEY || 'sk_test_test1234567890123456789test';
const BASE_URL = 'https://api.myemailverifier.com';

async function verifyBatch(emails) {
  try {
    console.log(`Verifying ${emails.length} emails in batch...`);

    const response = await axios.post(`${BASE_URL}/verify-batch`, {
      emails: emails,
      api_key: API_KEY
    });

    const result = response.data;

    // Display summary
    console.log('\n=== Batch Verification Summary ===');
    console.log(`Total Emails: ${result.total}`);
    console.log(`Valid: ${result.verified}`);
    console.log(`Invalid: ${result.invalid}`);

    // Display detailed results
    console.log('\n=== Detailed Results ===');
    result.results.forEach((item, index) => {
      console.log(`\n${index + 1}. ${item.email}`);
      console.log(`   Valid: ${item.is_valid}`);
      console.log(`   Deliverability: ${item.deliverability}`);
      console.log(`   Error Code: ${item.error_code}`);
    });

    return result;
  } catch (error) {
    console.error('Error verifying batch:');
    console.error(error.response?.data || error.message);
  }
}

async function main() {
  const emailList = [
    'john.doe@example.com',
    'jane.smith@example.com',
    'invalid-email@invalid-domain.com',
    'support@example.com',
    'contact@company.org'
  ];

  // Verify emails in batches (max 100 per batch)
  const batchSize = 100;
  for (let i = 0; i < emailList.length; i += batchSize) {
    const batch = emailList.slice(i, i + batchSize);
    await verifyBatch(batch);
    console.log('\n' + '='.repeat(50) + '\n');
  }
}

main();
