# 🤝 Contributing to MailFlow

Welcome to the MailFlow interview project! This guide will help you understand how to contribute effectively and showcase your skills.

## 🎯 Project Structure

```
mailflow-interview/
├── frontend/                 # React/Vue.js frontend application
├── backend/                  # Node.js/Python backend API
├── ai-service/              # LLM integration service
├── database/                # Database schemas and migrations
├── docker/                  # Docker configuration files
├── docs/                    # Additional documentation
├── .github/                 # GitHub templates and workflows
└── README.md               # Main project documentation
```

## 🚀 Getting Started

### 1. Fork and Clone
```bash
# Fork the repository on GitHub, then clone your fork
git clone https://github.com/YOUR_USERNAME/mailflow-interview.git
cd mailflow-interview
```

### 2. Set Up Development Environment
```bash
# Install dependencies for all services
npm run install:all
# or
make install
```

### 3. Create Your Development Branch
```bash
git checkout -b feature/your-name-phase-1
```

## 📋 Development Workflow

### Phase-Based Development
Work through the project in phases, creating separate branches for each:

```bash
# Phase 1: Core Platform
git checkout -b phase-1/your-name-core-platform

# Phase 2: AI Integration
git checkout -b phase-2/your-name-ai-integration

# Phase 3: Deployment
git checkout -b phase-3/your-name-deployment
```

### Commit Message Convention
Use conventional commits for clear history:

```bash
# Format: type(scope): description
git commit -m "feat(frontend): add email template editor"
git commit -m "fix(backend): resolve authentication middleware issue"
git commit -m "docs(readme): update setup instructions"
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

## 🔄 Pull Request Process

### 1. Before Creating a PR
- [ ] Code is tested and working
- [ ] Documentation is updated
- [ ] No console errors or warnings
- [ ] Code follows project style guidelines

### 2. Creating the PR
1. Push your branch to your fork
2. Create a Pull Request using the provided template
3. Fill out all sections of the PR template
4. Add screenshots/GIFs demonstrating functionality
5. Request review from the interview team

### 3. PR Review Process
- Reviews typically happen within 24 hours
- Address feedback promptly
- Keep discussions professional and constructive
- Be open to suggestions and improvements

## 🧪 Testing Guidelines

### Frontend Testing
```bash
# Run unit tests
npm run test:frontend

# Run e2e tests
npm run test:e2e

# Generate coverage report
npm run test:coverage
```

### Backend Testing
```bash
# Run API tests
npm run test:backend

# Run integration tests
npm run test:integration
```

### AI Service Testing
```bash
# Test LLM integrations
npm run test:ai

# Test prompt engineering
npm run test:prompts
```

## 📝 Code Style Guidelines

### JavaScript/TypeScript
- Use ESLint and Prettier configurations
- Follow functional programming principles where possible
- Use TypeScript for type safety
- Write self-documenting code with clear variable names

### Python
- Follow PEP 8 style guidelines
- Use type hints
- Write docstrings for functions and classes
- Use meaningful variable and function names

### General Guidelines
- Keep functions small and focused
- Use consistent naming conventions
- Comment complex logic
- Avoid deep nesting
- Handle errors gracefully

## 🏗️ Architecture Guidelines

### Frontend Architecture
- Component-based architecture
- State management with Redux/Zustand/Pinia
- Responsive design principles
- Accessibility considerations

### Backend Architecture
- RESTful API design
- Proper error handling
- Input validation
- Security best practices

### Database Design
- Normalized database schema
- Proper indexing
- Data validation
- Migration scripts

## 🤖 AI Integration Best Practices

### LLM Integration
- Implement proper error handling for API calls
- Use caching for repeated requests
- Implement rate limiting
- Monitor token usage

### Prompt Engineering
- Create reusable prompt templates
- Implement prompt versioning
- Test prompts thoroughly
- Document prompt strategies

## 🚀 Deployment Guidelines

### Docker
- Multi-stage builds for optimization
- Proper environment variable handling
- Health checks for containers
- Security scanning

### Cloud Deployment
- Infrastructure as Code (IaC)
- Proper secrets management
- Monitoring and logging
- Auto-scaling configuration

## 📊 Performance Guidelines

### Frontend Performance
- Code splitting and lazy loading
- Image optimization
- Bundle size optimization
- Caching strategies

### Backend Performance
- Database query optimization
- API response caching
- Connection pooling
- Load balancing considerations

## 🔒 Security Guidelines

### Authentication & Authorization
- Secure password handling
- JWT token management
- Role-based access control
- Session management

### Data Protection
- Input sanitization
- SQL injection prevention
- XSS protection
- CORS configuration

## 📚 Documentation Standards

### Code Documentation
- Clear README files for each service
- API documentation (OpenAPI/Swagger)
- Inline code comments
- Architecture decision records (ADRs)

### User Documentation
- Setup and installation guides
- Feature documentation
- Troubleshooting guides
- FAQ sections

## 🆘 Getting Help

### Communication Channels
- **Slack**: #mailflow-interview
- **Email**: interview-support@company.com
- **Office Hours**: Mon-Fri, 2-4 PM IST

### When to Ask for Help
- Stuck on a technical problem for >2 hours
- Unclear about requirements
- Need clarification on evaluation criteria
- Facing environment setup issues

### How to Ask for Help
1. Describe the problem clearly
2. Share relevant code snippets
3. Explain what you've already tried
4. Include error messages and logs
5. Specify your environment details

## 🏆 Evaluation Criteria

Your contribution will be evaluated on:

| Criteria | Weight | Description |
|----------|--------|-------------|
| **Code Quality** | 25% | Clean, readable, maintainable code |
| **Functionality** | 25% | Features work as expected |
| **AI Integration** | 20% | Creative and effective use of GenAI |
| **Architecture** | 15% | System design and scalability |
| **Documentation** | 10% | Clear setup and usage instructions |
| **Innovation** | 5% | Creative solutions and extra features |

## 🎉 Recognition

Outstanding contributions will be recognized through:
- Mention in project credits
- LinkedIn recommendations
- Potential fast-track for future opportunities
- Open source contribution portfolio

## 📄 License

By contributing to this project, you agree that your contributions will be licensed under the MIT License.

---

**Happy coding! We're excited to see what you build! 🚀**