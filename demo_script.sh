#!/bin/bash

# ============================================
# BOB AI ASSISTANT - QUICK DEMONSTRATION SCRIPT
# ============================================
# This bash script demonstrates Bob's capabilities
# Run with: bash demo_script.sh or ./demo_script.sh

# Colors
CYAN='\033[0;36m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
WHITE='\033[1;37m'
GRAY='\033[0;37m'
NC='\033[0m' # No Color

# Function to pause and wait for user
pause_demo() {
    echo ""
    echo -e "${YELLOW}Press Enter to continue...${NC}"
    read -r
}

# Header
echo -e "${CYAN}========================================${NC}"
echo -e "${CYAN}IBM Bob AI Assistant Demonstration${NC}"
echo -e "${CYAN}Project: RepoPilot${NC}"
echo -e "${CYAN}========================================${NC}"
echo ""

# 1. Show Project Structure
echo -e "${GREEN}=== STEP 1: Project Structure ===${NC}"
echo -e "${WHITE}Displaying RepoPilot project structure...${NC}"
tree -L 2 -d || find . -type d -maxdepth 2 | grep -v ".git"
pause_demo

# 2. Display README
echo -e "${GREEN}=== STEP 2: Project Overview ===${NC}"
echo -e "${WHITE}Reading README.md...${NC}"
head -n 30 README.md
echo -e "${GRAY}... (truncated for demo)${NC}"
pause_demo

# 3. Run Sample Application
echo -e "${GREEN}=== STEP 3: Running Sample Calculator ===${NC}"
echo -e "${WHITE}Executing sample_repo/main.py...${NC}"
cd sample_repo
python3 main.py || python main.py
cd ..
pause_demo

# 4. Test Calculator Functions
echo -e "${GREEN}=== STEP 4: Testing Calculator Functions ===${NC}"
echo -e "${WHITE}Running interactive calculator tests...${NC}"

cd sample_repo
python3 << 'EOF' || python << 'EOF'
from calculator import add, subtract, multiply, divide

print('Testing add(15, 25):', add(15, 25))
print('Testing subtract(50, 20):', subtract(50, 20))
print('Testing multiply(7, 8):', multiply(7, 8))
print('Testing divide(100, 5):', divide(100, 5))

try:
    divide(10, 0)
except ValueError as e:
    print('Testing divide by zero - Error:', e)
EOF
cd ..
pause_demo

# 5. Show Generated Documentation
echo -e "${GREEN}=== STEP 5: Generated Documentation ===${NC}"
echo -e "${WHITE}Listing documentation files...${NC}"
ls -lh generated_docs/
echo ""
echo -e "${WHITE}Preview of architecture_overview.md:${NC}"
head -n 20 generated_docs/architecture_overview.md
echo -e "${GRAY}... (truncated for demo)${NC}"
pause_demo

# 6. Show Generated Tests
echo -e "${GREEN}=== STEP 6: Generated Tests ===${NC}"
echo -e "${WHITE}Displaying test files...${NC}"
ls -lh generated_tests/
echo ""
echo -e "${WHITE}Preview of test_core.py:${NC}"
head -n 25 generated_tests/test_core.py
echo -e "${GRAY}... (truncated for demo)${NC}"
pause_demo

# 7. Code Analysis
echo -e "${GREEN}=== STEP 7: Code Analysis ===${NC}"
echo -e "${WHITE}Analyzing calculator.py...${NC}"
CALC_FILE="sample_repo/calculator.py"
LINE_COUNT=$(wc -l < "$CALC_FILE")
echo -e "${CYAN}Total lines: $LINE_COUNT${NC}"
echo ""
echo -e "${WHITE}Function definitions found:${NC}"
grep -n "^def " "$CALC_FILE" | while read -r line; do
    echo -e "  ${CYAN}$line${NC}"
done
pause_demo

# 8. File Statistics
echo -e "${GREEN}=== STEP 8: Project Statistics ===${NC}"
echo -e "${WHITE}Calculating project metrics...${NC}"
PY_COUNT=$(find . -name "*.py" -type f | wc -l)
MD_COUNT=$(find . -name "*.md" -type f | wc -l)
echo -e "${CYAN}Python files: $PY_COUNT${NC}"
echo -e "${CYAN}Markdown files: $MD_COUNT${NC}"
echo ""
echo -e "${WHITE}Total lines of Python code:${NC}"
TOTAL_LINES=0
find . -name "*.py" -type f | while read -r file; do
    LINES=$(wc -l < "$file")
    TOTAL_LINES=$((TOTAL_LINES + LINES))
    echo -e "  ${CYAN}$(basename "$file"): $LINES lines${NC}"
done
pause_demo

# 9. Demonstration Complete
echo ""
echo -e "${CYAN}========================================${NC}"
echo -e "${GREEN}Demonstration Complete!${NC}"
echo -e "${CYAN}========================================${NC}"
echo ""
echo -e "${WHITE}Bob AI Assistant successfully demonstrated:${NC}"
echo -e "${GREEN}  [OK] Project structure analysis${NC}"
echo -e "${GREEN}  [OK] Code execution and testing${NC}"
echo -e "${GREEN}  [OK] Documentation generation${NC}"
echo -e "${GREEN}  [OK] Test suite creation${NC}"
echo -e "${GREEN}  [OK] Code analysis and metrics${NC}"
echo ""
echo -e "${YELLOW}For more details, see BOB_DEMONSTRATION.md${NC}"
echo ""

# Made with Bob
