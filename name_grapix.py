# Function to create a bordered box around the text
def create_bordered_text(text):
    lines = text.split('\n')
    max_length = max(len(line) for line in lines)
    border = '╔' + '═' * (max_length + 2) + '╗\n'
    result = border

    for line in lines:
        spaces = max_length - len(line)
        result += f'║ {line}{" " * spaces} ║\n'

    result += border
    return result
def name():
    # Define ASCII art for the letters 'p', 't', 'p'
    letter_p = [
        "██████╗ ",
        "██╔══██╗",
        "██████╔╝",
        "██╔═══╝ ",
        "██║     ",
    ]

    letter_t = [
        "████████╗",
        "╚══██╔══╝",
        "   ██║   ",
        "   ██║   ",
        "   ╚═╝   ",
    ]

    # Combine the letters to form "ptp" in ASCII art
    text_ptp = [
        letter_p, letter_t, letter_p
    ]

    # Join the ASCII art for 'ptp'
    ptp_art = ''
    for i in range(5):
        for letter in text_ptp:
            ptp_art += letter[i] + '  '
        ptp_art += '\n'

    # Create the bordered text
    welcome_text = "Welcome to PTP Bruteforcer"
    made_by_text = "Made by Philotheephilix"

    # Create the bordered box with the centered text
    bordered_welcome = create_bordered_text(welcome_text.center(45))
    bordered_made_by = create_bordered_text(made_by_text.center(45))

    # Combine all bordered text into one layout
    full_layout = bordered_welcome + '\n\n' + ptp_art + '\n\n' + bordered_made_by

    # Create a giant border around the whole layout
    full_layout_bordered = create_bordered_text(full_layout)

    # Print the result
    print(full_layout_bordered)
            