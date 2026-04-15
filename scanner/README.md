## Rozpoznawane tokeny przez skaner

### Operatory porównania
| Nazwa tokena        | Id tokena | Regex |
|---------------------|----------|-------|
| Równe               | EQ       | `=` |
| Mniejsze            | LT       | `<` |
| Mniejsze lub równe  | LE       | `<=` |
| Większe             | GT       | `>` |
| Większe lub równe   | GE       | `>=` |

### Nawiasy
| Nazwa tokena        | Id tokena     | Regex |
|---------------------|--------------|-------|
| Lewy nawias okrągły | leftParen    | `\(` |
| Prawy nawias okrągły| rightParen   | `\)` |
| Lewa klamra         | leftBrace    | `{` |
| Prawa klamra        | rightBrace   | `}` |
| Lewy nawias kwadratowy | leftBracket | `\[` |
| Prawy nawias kwadratowy | rightBracket | `\]` |

### Operatory arytmetyczne
| Nazwa tokena      | Id tokena | Regex |
|-------------------|----------|-------|
| Plus              | plusSign | `\+` |
| Minus             | minusSign| `-` |
| Mnożenie          | multSign | `\*` |
| Dzielenie         | divSign  | `/` |

### Operatory logiczne
| Nazwa tokena | Id tokena | Regex |
|--------------|----------|-------|
| AND          | LOGIC_AND| `&&` |
| OR           | LOGIC_OR | `\|\|` |

### Inne operatory
| Nazwa tokena        | Id tokena              | Regex |
|---------------------|------------------------|-------|
| Operator adresu     | ADDRESS_OF_OPERATOR    | `&` |

### Separatory
| Nazwa tokena | Id tokena | Regex |
|--------------|----------|-------|
| Przecinek    | COMMA    | `,` |
| Kropka       | DOT      | `\.` |
| Średnik      | COLON    | `;` |

### Słowa kluczowe
| Nazwa | Id tokena | Regex |
|------|----------|-------|
| if   | IF       | `if` |
| else | ELSE     | `else` |
| for  | FOR      | `for` |
| while| WHILE    | `while` |
| begin| BEGIN    | `begin` |
| end  | END      | `end` |

*(rozpoznawane bez uwzględniania wielkości liter)*

### Typy danych
| Nazwa  | Id tokena   | Regex |
|--------|------------|-------|
| int    | INT_TYPE   | `int` |
| float  | FLOAT_TYPE | `float` |
| double | DOUBLE_TYPE| `double` |
| char   | CHAR_TYPE  | `char` |
| bool   | BOOL_TYPE  | `bool` |
| void   | VOID_TYPE  | `void` |

### Literały
| Nazwa tokena        | Id tokena           | Regex |
|---------------------|---------------------|-------|
| Liczba całkowita    | number              | `[0-9]+` |
| String              | STRING              | `".*"` |
| Niedomknięty string | UNFINISHED_STRING   | `"[^"]*` |

### Identyfikatory
| Nazwa tokena | Id tokena | Regex |
|--------------|----------|-------|
| Identyfikator| id       | `[a-zA-Z][a-zA-Z0-9]*` |

### Białe znaki
| Nazwa tokena | Id tokena | Regex |
|--------------|----------|-------|
| Spacja       | SPACE    | `" "` |
| Nowa linia   | NEWLINE  | `\n` |

### Inne
| Nazwa tokena | Id tokena | Opis |
|--------------|----------|------|
| Koniec pliku | EOF      | koniec wejścia |
| Nieznany     | UNKNOWN  | nierozpoznany token |

---

## Dodatkowe informacje

- Skaner działa sekwencyjnie, czytając plik znak po znaku.
- Token jest maksymalnie wydłużany (greedy matching), dopóki kolejny znak nie powoduje powstania nieznanego tokena.
- Słowa kluczowe i typy są rozpoznawane **case-insensitive**.
- Stringi muszą być ujęte w cudzysłowy (`"`), w przeciwnym razie są oznaczane jako `UNFINISHED_STRING`.
- Liczby aktualnie obsługują tylko liczby całkowite (`int`).