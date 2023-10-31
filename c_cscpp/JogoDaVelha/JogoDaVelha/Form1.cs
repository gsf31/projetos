class TicTacToe
{
    static void Main(string[] args)
    {
        // Cria o tabuleiro
        int[,] board = new int[3, 3];
        for (int i = 0; i < 3; i++)
        {
            for (int j = 0; j < 3; j++)
            {
                board[i, j] = -1;
            }
        }

        // Inicializa as variáveis do jogo
        int turn = 0; // 0 = X, 1 = O
        bool gameOver = false;

        // Loop principal do jogo
        while (!gameOver)
        {
            // Mostra o tabuleiro atual
            ShowBoard(board);

            // Recebe a jogada do jogador
            int row, col;
            do
            {
                Console.Write("Jogador {0}: Digite a linha e a coluna da sua jogada (1-3): ", turn + 1);
                row = Convert.ToInt32(Console.ReadLine());
                col = Convert.ToInt32(Console.ReadLine());
            } while (row < 1 || row > 3 || col < 1 || col > 3 || board[row - 1, col - 1] != -1);

            // Faz a jogada
            board[row - 1, col - 1] = turn + 1;

            // Verifica se o jogo terminou
            gameOver = CheckGame(board);

            // Troca de turno
            turn = 1 - turn;
        }

        // Mostra o resultado do jogo
        if (gameOver)
        {
            ShowBoard(board);
            Console.WriteLine("O jogador {0} ganhou!", turn + 1);
        }
        else
        {
            Console.WriteLine("O jogo empatou!");
        }
    }

    // Mostra o tabuleiro
    static void ShowBoard(int[,] board)
    {
        for (int i = 0; i < 3; i++)
        {
            for (int j = 0; j < 3; j++)
            {
                switch (board[i, j])
                {
                    case -1:
                        Console.Write(" ");
                        break;
                    case 0:
                        Console.Write("X");
                        break;
                    case 1:
                        Console.Write("O");
                        break;
                }
            }
            Console.WriteLine();
        }
    }

    // Verifica se o jogo terminou
    static bool CheckGame(int[,] board)
    {
        // Verifica se um jogador ganhou
        for (int i = 0; i < 3; i++)
        {
            if (board[i, 0] == board[i, 1] && board[i, 1] == board[i, 2] && board[i, 0] != -1)
            {
                return true;
            }
            if (board[0, i] == board[1, i] && board[1, i] == board[2, i] && board[0, i] != -1)
            {
                return true;
            }
        }
        if (board[0, 0] == board[1, 1] && board[1, 1] == board[2, 2] && board[0, 0] != -1)
        {
            return true;
        }
        if (board[0, 2] == board[1, 1] && board[1, 1] == board[2, 0] && board[0, 2] != -1)
        {
            return true;
        }

        // Verifica se o jogo empatou
        for (int i = 0; i < 3; i++)
        {
            for (int j = 0; j < 3; j++)
            {
                if (board[i, j] == -1)
                {
                    return false;
                }
            }
        }

        // O jogo empatou
        return true;
    }
}