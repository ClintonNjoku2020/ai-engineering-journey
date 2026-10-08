# AI Engineering Environment Setup

This document explains the development environment I set up for the AI Engineering Program. The setup provides me with a Linux development environment, Python with isolated virtual environments, Git and GitHub for version control, SSH authentication, a terminal-based AI coding assistant, and access to a remote server for publishing my work.

## Ubuntu

I installed Ubuntu through Windows Subsystem for Linux 2 (WSL2) to provide a Linux development environment on my Windows computer. Linux is widely used for AI infrastructure, including servers, cloud instances, GPU machines, and containers. Using Ubuntu through WSL2 allows me to learn and practise Linux commands while continuing to use Windows as my main desktop environment. This will help me become familiar with the type of environment commonly used for professional AI engineering work.

## Python and Virtual Environments

Python is one of the main programming languages I will use for AI engineering, including data analysis and machine learning. I installed Python, pip, and the tools required to create virtual environments. I created a virtual environment called `venv` inside my AI Engineering workspace and installed libraries such as NumPy, Pandas, and Jupyter in it. The virtual environment keeps the dependencies for my projects isolated, which helps prevent different projects from interfering with each other or requiring conflicting library versions.

## Git and GitHub

Git is the version control system I use to record changes to my projects and maintain a history of my work. GitHub provides the online repository where my projects can be stored and shared. I configured Git with my name and GitHub email address and created an `ai-engineering-journey` repository. I also created a README file and configured Git to use `main` as the default branch. Using Git and GitHub will allow me to track my work, make changes safely, and maintain a record of my progress throughout the AI Engineering program.

## SSH Keys

I created an SSH key pair to authenticate securely with GitHub without relying on a password each time I connect. The key pair consists of a public key and a private key. I added the public key to my GitHub account and tested the connection using SSH. The public key can be shared with services such as GitHub, while the private key must remain confidential. I will never share or commit my private SSH key to a repository because anyone who obtains it could potentially use it to authenticate as me.

## Node.js and AI Assistant

I installed Node.js because the terminal-based AI coding assistant used in this setup requires Node.js version 22 or newer. I installed Node using a version manager and then installed Claude Code as the terminal AI assistant. The assistant can help me work with code directly from my project environment. However, I understand that using an AI coding assistant does not remove the need to understand and verify its output. I need to review what the assistant produces and check that it is correct before using it in my projects.

## Remote Server

The remote server provides an environment where I can connect remotely and publish my work so that it can be accessed through a web address. During the setup, I used SSH to connect to the server and created my own project folder. I also set up a subdomain and published a simple web page. This gives me practical experience of moving beyond local development and deploying work to a live environment. Server credentials are confidential and must not be shared, committed to Git, or published online.

## Conclusion

This setup gives me the foundation for professional AI engineering work. I now have a Linux environment, Python development environment, version control with Git and GitHub, secure SSH authentication, a terminal AI assistant, and access to a remote server. I will use this environment throughout the program to build, test, document, version, and publish my AI engineering projects.
