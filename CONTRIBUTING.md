# Contributing to MyEmailVerifier API

We welcome contributions from the community! This document provides guidelines and instructions for contributing.

## 📋 Code of Conduct

Please note that we have adopted a Code of Conduct. We expect all contributors to adhere to it. Any violations should be reported to conduct@myemailverifier.com.

---

## 🤝 Types of Contributions

### 🐛 Reporting Bugs

Found a bug? Please report it using GitHub Issues:

1. Check if the bug already exists
2. Provide a clear title and description
3. Include steps to reproduce
4. Share expected vs. actual behavior
5. Include your environment details:
   - API version
   - Language/SDK version
   - Operating system
   - Error messages

**Example:**
```
Title: API returns 500 error for valid emails

Description:
When verifying emails with certain domains, the API returns a 500 error
instead of a valid response.

Steps to reproduce:
1. Call /verify endpoint with email "user@specific-domain.com"
2. API returns 500 error
3. Error persists for multiple attempts

Expected behavior:
API should return verification status

Environment:
- API Version: 1.0
- Language: Python 3.8
- OS: macOS 12
```

### ✨ Feature Requests

Have an idea? Open a GitHub Discussion or Issue:

1. Clearly describe the feature
2. Explain the use case and benefits
3. Provide examples
4. Discuss alternative solutions

**Example:**
```
Title: Add bulk download as CSV feature

Description:
It would be helpful to download batch verification results as CSV format
for integration with spreadsheet applications.

Use case:
Marketing teams often need to export results to Excel for segmentation.

Example:
GET /download-results/{batch_id}?format=csv
```

### 📖 Documentation

Help improve our documentation:

1. Fix typos and grammar
2. Clarify confusing sections
3. Add examples
4. Translate to other languages
5. Improve code samples

### 💻 Code Contributions

Join us in improving the codebase:

1. **SDKs** - Contribute language-specific SDKs
2. **Examples** - Add integration examples
3. **Libraries** - Build helper libraries
4. **Tools** - Create useful tools and utilities

---

## 🚀 Getting Started

### Fork and Clone

```bash
# Fork the repository on GitHub
# Then clone your fork
git clone https://github.com/YOUR_USERNAME/myemailverifier-api.git
cd myemailverifier-api

# Add upstream remote
git remote add upstream https://github.com/myemailverifier/api.git
```

### Create a Branch

```bash
# Update main branch
git checkout main
git pull upstream main

# Create feature branch
git checkout -b feature/your-feature-name
# or
git checkout -b fix/issue-number
```

### Make Changes

1. Make your changes
2. Follow coding standards
3. Add tests if applicable
4. Update documentation
5. Test thoroughly

### Commit Changes

```bash
# Use clear, descriptive commit messages
git commit -m "feat: add new verification method"
git commit -m "fix: resolve rate limiting issue"
git commit -m "docs: clarify authentication process"
```

**Commit message format:**
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation
- `style:` - Code style
- `refactor:` - Code refactoring
- `test:` - Test additions
- `chore:` - Maintenance

### Push and Create Pull Request

```bash
# Push to your fork
git push origin feature/your-feature-name

# Create Pull Request on GitHub
```

### Pull Request Checklist

- [ ] Branch is up to date with main
- [ ] Tests pass
- [ ] Code follows style guidelines
- [ ] Documentation is updated
- [ ] Commit messages are clear
- [ ] No unnecessary files included

---

## 📝 Code Standards

### JavaScript/Node.js
- Use ES6+ syntax
- Follow [Airbnb style guide](https://github.com/airbnb/javascript)
- Use async/await over callbacks
- Include JSDoc comments

### Python
- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Use type hints
- Include docstrings
- Target Python 3.6+

### PHP
- Follow [PSR-12](https://www.php-fig.org/psr/psr-12/)
- Use type declarations
- Include PHPDoc comments
- Target PHP 7.2+

### General
- Keep functions small and focused
- Use descriptive names
- Add comments for complex logic
- Keep code DRY (Don't Repeat Yourself)

---

## 🧪 Testing

### Running Tests

```bash
# Node.js
npm test

# Python
pytest

# PHP
phpunit
```

### Adding Tests

- Write tests for new features
- Ensure existing tests pass
- Aim for >80% code coverage
- Test error cases

---

## 📚 Documentation Standards

### File Structure
```
docs/
  - README.md         # Overview
  - GETTING_STARTED.md # Setup guide
  - API_REFERENCE.md  # Complete API docs
  - EXAMPLES.md       # Code examples
```

### Writing Guidelines

- Use clear, concise language
- Include practical examples
- Provide code samples
- Link to related docs
- Keep it up to date

---

## 🔐 Security

### Reporting Security Issues

**Please do not open public issues for security vulnerabilities.**

Instead, email security@myemailverifier.com with:
- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Your contact information

We'll respond within 48 hours.

### Security Best Practices

- Don't commit API keys or secrets
- Validate user input
- Use HTTPS for all communications
- Keep dependencies updated
- Follow OWASP guidelines

---

## 📦 Release Process

### Version Numbering

We follow [Semantic Versioning](https://semver.org/):
- `MAJOR.MINOR.PATCH`
- `1.2.3` = Version 1, Minor 2, Patch 3

### Changelog

Update `CHANGELOG.md` with:
- Features added
- Bugs fixed
- Breaking changes
- Deprecations

---

## 💬 Communication

### Getting Help

- **GitHub Issues** - Bug reports and feature requests
- **GitHub Discussions** - Questions and ideas
- **Email** - support@myemailverifier.com
- **Discord** - Community server (coming soon)

### Community Guidelines

- Be respectful and inclusive
- No harassment or discrimination
- Collaborative problem-solving
- Assume good intentions
- Welcome diverse perspectives

---

## 🎁 Rewards

### Recognition

Contributors will be:
- Listed in CONTRIBUTORS.md
- Mentioned in release notes
- Featured in community updates

### Swag

Top contributors get:
- MyEmailVerifier swag
- Priority support
- Free premium account

---

## 📋 Review Process

### What We Review

1. Code quality and style
2. Test coverage
3. Documentation
4. Performance impact
5. Security implications
6. Backwards compatibility

### Timeline

- Initial response: Within 1 week
- Detailed review: Within 2 weeks
- Approval or feedback: Within 3 weeks

### Feedback

Constructive feedback is provided to improve the contribution and help you learn.

---

## ✅ Final Checklist

Before submitting your PR:

- [ ] Fork and clone the repo
- [ ] Test your changes locally
- [ ] Update documentation
- [ ] Add/update tests
- [ ] Follow code standards
- [ ] Clear, descriptive commit messages
- [ ] No merge conflicts
- [ ] No breaking changes (unless necessary)

---

## 🙏 Thank You

Thank you for contributing to MyEmailVerifier API! Your efforts help make email verification better for everyone.

---

**Questions? Feel free to reach out to us!**

- 📧 Email: support@myemailverifier.com
- 💬 GitHub: Open an issue or discussion
- 🌐 Website: [MyEmailVerifier.com](https://myemailverifier.com)
