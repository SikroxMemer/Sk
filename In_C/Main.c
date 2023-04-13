#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#define MAX_INTEGER_LENGTH 100
/*
Basic S# TokenTypes , C Like Tokens Doesn't support floats :
typeof TokenType => enum
*/
typedef enum
{
    TOKEN_INTEGER,
    TOKEN_PLUS,
    TOKEN_MINUS,
    TOKEN_MULTIPLY,
    TOKEN_DIVIDE,
    TOKEN_LPAREN,
    TOKEN_RPAREN,
    TOKEN_EOF,
} TokenType;
/*
S# Struct Object Constructor , it contains :
type => enum TokenType
value => int
*/
typedef struct
{
    TokenType type;
    int value;
} Token;

Token Tokens[MAX_INTEGER_LENGTH];
int Number_Tokens = 0;
/*
S# Tokenizer , function
*/
void Tokenize(const char *input)
{
    const char *pointer = input;
    while (*pointer)
    {
        if (isdigit(*pointer))
        {
            int value = 0;
            while (isdigit(*pointer))
            {
                value = value * 10 + (*pointer - '0');
                ++pointer;
            }
            Tokens[Number_Tokens].type = TOKEN_INTEGER;
            Tokens[Number_Tokens].value = value;
            ++Number_Tokens;
        }
        else if (*pointer == '+')
        {
            Tokens[Number_Tokens].type = TOKEN_PLUS;
            ++Number_Tokens;
            ++pointer;
        }
        else if (*pointer == '-')
        {
            Tokens[Number_Tokens].type = TOKEN_MINUS;
            ++Number_Tokens;
            ++pointer;
        }
        else if (*pointer == '/')
        {
            Tokens[Number_Tokens].type = TOKEN_DIVIDE;
            ++Number_Tokens;
            ++pointer;
        }
        else if (*pointer == '*')
        {
            Tokens[Number_Tokens].type = TOKEN_MULTIPLY;
            ++Number_Tokens;
            ++pointer;
        }
        else if (*pointer == ')')
        {
            Tokens[Number_Tokens].type = TOKEN_LPAREN;
            ++Number_Tokens;
            ++pointer;
        }
        else if (*pointer == '(')
        {
            Tokens[Number_Tokens].type = TOKEN_RPAREN;
            ++Number_Tokens;
            ++pointer;
        }
        else
        {
            fprintf(stderr, "Error : Invalid Character '%c'\n", *pointer);
            exit(1);
        }
    }
    Tokens[Number_Tokens].type = TOKEN_EOF;
};

int expr();

int factor()
{
    Token token = Tokens[Number_Tokens++];
    if (token.type == TOKEN_INTEGER)
    {
        return token.value;
    }
    else if (token.type == TOKEN_LPAREN)
    {
        int value = expr();
        if (Tokens[Number_Tokens++].type != TOKEN_RPAREN)
        {
            fprintf(stderr, "Error : Expected ')' \n");
            exit(1);
        }
        return value;
    }
    else
    {
        fprintf(stderr, "Error : Expected integer or '(' got %d\n", token.type);
        exit(1);
    }
};

int term()
{
    int value = factor();
    while (Tokens[Number_Tokens].type == TOKEN_MULTIPLY || Tokens[Number_Tokens].type == TOKEN_DIVIDE)
    {
        Token token = Tokens[Number_Tokens++];

        if (token.type == TOKEN_MULTIPLY)
            value *= factor();
        else
            value /= factor();
    }

    return value;
}

int expr()
{
    int value = term();

    while (Tokens[Number_Tokens].type == TOKEN_PLUS || Tokens[Number_Tokens].type == TOKEN_MINUS)
    {
        Token token = Tokens[Number_Tokens++];

        if (token.type == TOKEN_PLUS)
            value += term();
        else
            value -= term();
    }

    return value;
}

int main()
{
    char input[100];

    printf("Enter an expression: ");
    fgets(input, 100, stdin);

    input[strcspn(input, "\n")] = '\0';

    Tokenize(input);

    int result = expr();

    printf("Result: %d\n", result);

    return 0;
}