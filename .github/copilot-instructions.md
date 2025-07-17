# GitHub Copilot Instructions for BAM Summer Mentorship Program - Intermediate Python Programming

## Important Note on Student Devices

**All students will be using Windows machines.**

- When providing instructions, code, or keyboard shortcuts, always ensure they are applicable to Windows systems or to GitHub Codespaces accessed with a Windows keyboard layout.
- Avoid recommending Mac-specific commands, shortcuts, or tools unless they are also valid on Windows.
- If suggesting terminal commands, use Windows Command Prompt, PowerShell, or Windows-compatible instructions, or specify if the command is for Codespaces.
- For Codespaces, assume students are using a Windows keyboard and highlight any differences in shortcuts or behavior if relevant.

## Workspace Structure
This repository contains materials for the "Intermediate Python Programming" program, which is organized as a 3-lesson curriculum exploring Python graphics programming and GitHub collaboration:

- `lesson-1/`: Turtle Graphics Programming
  - Focus: Python turtle graphics, visual programming, creative coding
  - Topics: Turtle module, coordinate systems, loops, functions, colors, patterns
  - Projects: Flower gardens, star patterns, house scenes, target practice
  - Key files: `README.md`, `main.py`
  - Skills: Drawing shapes, using colors, creating patterns, algorithmic thinking

- `lesson-2/`: [Future Lesson - Currently Empty]
  - Placeholder for future intermediate Python concepts
  - Will build upon turtle graphics foundation

- `lesson-3/`: [Future Lesson - Currently Empty]  
  - Placeholder for future advanced Python concepts
  - Will integrate previous lessons into more complex projects

- `img/`: Contains images and graphics used throughout the lessons and documentation

## Student Context
- Students have completed the introductory Python course and have basic programming knowledge
- The course focuses on intermediate-level Python programming with visual feedback
- Students will work primarily with Python's built-in turtle module (no external libraries required)
- Each lesson builds upon previous knowledge, progressing from basic graphics to more complex programming concepts
- Students should complete projects and assessments to demonstrate mastery of Python programming techniques

## Turtle Graphics Programming Focus

**This course emphasizes visual programming using Python's built-in turtle module.**

- All graphics projects use the built-in `turtle` module - no external libraries needed
- Students learn programming concepts through visual feedback and creative projects
- Focus on algorithmic thinking, loops, functions, and coordinate geometry
- Encourage experimentation with colors, patterns, and artistic expression
- Help students understand the connection between code and visual output

## Graphics and Visual Programming Guidelines

**For turtle graphics projects, emphasize visual learning and creative expression.**

- Use the turtle module's built-in coordinate system and drawing functions
- Encourage students to experiment with different colors, shapes, and patterns
- Help students understand how mathematical concepts translate to visual output
- Guide students to break complex drawings into smaller, manageable functions
- Emphasize the iterative process of coding, testing, and refining visual output

Example turtle graphics patterns:
```python
import turtle

# Simple flower pattern
def draw_flower():
    for i in range(6):
        turtle.circle(50)
        turtle.right(60)
```

## Application Execution Guidelines

**Students should use VS Code's built-in Run and Debug functionality to execute their applications.**

- Avoid suggesting commands like `python main.py` unless specifically requested
- Students are expected to use VS Code's Run and Debug features (F5 key or the Run button in VS Code)
- For Python applications, guide students to use VS Code's Python extension and integrated terminal
- Focus on code development and debugging rather than manual command-line execution
- Encourage students to test their code frequently to see visual results

## When Assisting Students

1. **Identify the current lesson context** based on the folder structure and student's location
2. **For lesson-1 (Turtle Graphics Programming):**
   - Focus on turtle module functions and coordinate systems
   - Help with drawing shapes, using colors, and creating patterns
   - Assist with loops, functions, and algorithmic thinking
   - Guide students through the four main project types: flowers, stars, houses, and targets
   - Encourage creative experimentation and artistic expression

3. **For future lessons (lesson-2 and lesson-3):**
   - These are currently empty and will be developed later
   - When developed, they will build upon turtle graphics foundation
   - Guide students to complete lesson-1 before moving to future lessons

4. **General guidance:**
   - Encourage iterative development and frequent testing
   - Connect programming concepts to visual output
   - Provide Windows-compatible instructions and shortcuts
   - Keep explanations appropriate for intermediate-level students
   - Foster creativity and artistic expression through code

## Python Programming Best Practices

**This course emphasizes good programming practices through visual projects.**

- Encourage students to write clean, readable code with meaningful variable names
- Guide students to break complex drawings into smaller functions
- Help students understand the importance of comments and documentation
- Emphasize the iterative process of coding, testing, and refining
- Connect programming concepts to mathematical and artistic principles

## GitHub Collaboration and Version Control

**Students will learn professional development practices through GitHub.**

- Guide students through the complete GitHub workflow: clone, code, commit, push
- Help students understand the importance of version control in software development
- Encourage students to try each other's projects and provide constructive feedback
- Teach students to use GitHub Issues for collaboration and feedback
- Emphasize professional communication and code sharing practices

## Windows Device Guidance

- All technical recommendations, troubleshooting steps, and keyboard shortcuts should be tailored for Windows users
- If a step differs between Windows and other operating systems, provide the Windows version first
- When referencing file paths, use Windows-style paths unless working in Codespaces
- For VS Code, assume students are using the Windows version or Codespaces in a browser

## Project Context
This repository is part of the Blacks at Microsoft (BAM) Summer Mentorship Program, designed to teach intermediate-level Python programming through visual graphics projects. Students learn fundamental programming concepts while creating artistic and creative visual outputs using Python's turtle module, building a foundation for more advanced programming concepts.