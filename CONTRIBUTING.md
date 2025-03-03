# Contributing to Theme Prompt Clash

We're excited that you're interested in contributing to Theme Prompt Clash! This document provides guidelines and instructions for contributing to the project.

## Getting Started

1. Fork the repository
2. Clone your fork locally
3. Install dependencies as described in the [Prerequisites](#prerequisites) section
4. Create a new branch for your feature/fix
5. Make your changes
6. Submit a pull request

## Prerequisites

Before you begin, ensure you have installed:

- Python 3.9.2
- Node.js 22.13.1
- MySQL 8.0 or later
- Poetry 2.0.1
- pnpm
- Docker and Docker Compose (for containerized deployment)

For detailed installation instructions, refer to the [INSTALLATION.md](./INSTALLATION.md).

## Development Workflow

1. Check existing issues and discussions before starting work
2. Create a new issue for features/bugs if one doesn't exist
3. Follow the coding style guidelines
4. Write tests for new features
5. Update documentation as needed
6. Ensure all tests pass before submitting PR

## Future Improvements

This is currently a demo version with several important features still in development:

### Image Selection
- Currently, only the last generated image per user is considered for the round
- Need to implement user ability to review and select their preferred image from all generations during the round
- Plan to add a gallery view for users to compare their generated images before final submission

### Winner Selection Process
- Current winner selection is manual and designed for live events
- Need to implement:
  - Frontend UI for automated voting/selection
  - Points system and user rankings
  - Potential AI-powered judging using LLMs to evaluate creativity and theme adherence

### Chat Management
- Chat sessions need to be:
  - Automatically created and linked to specific game rounds
  - Cleared between rounds
  - Managed by the system rather than user-initiated
- Implement proper round-chat synchronization and lifecycle management

We are open to receive contributions!