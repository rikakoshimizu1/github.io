import java.util.Random;

public class LizardCAGeneratorEfficient 
{
	public static void main(String[] args)
	{
		//Create an array
		int[][] array = new int[10][10];
		
		//Character of either 0 for Black or 1 for Green
		
		//Randomize 
		Random random = new Random();
		
		//Title
		System.out.println("Original");
		//Loop through entire outer loop
		for(int i=0; i<array.length; i++)
		{
			//Loop through entire inner loop
			for(int j=0; j<array[i].length; j++)
			{
				array[i][j] = random.nextInt(2);
				//Create spacing in between the numbers
				System.out.print(array[i][j] + "  ");
			}	
			System.out.println();
		}
		System.out.println();
		checkForGreen(array);
	}
	
	static int [][] countGreenArray = new int[10][10];
	static int [][] newArray = new int[10][10];
	
	public static final String ANSI_RESET = "\u001B[0m";
	public static final String ANSI_BLACK = "\u001B[30m";
	public static final String ANSI_GREEN = "\u001B[32m";
	
	public static void checkForGreen(int[][] array)
	{
		//Duplicate Array
		for(int i=0; i<array.length; i++)
		{
			countGreenArray[i] = array[i].clone();
			newArray[i] = array[i].clone();
		}
		
		int countGreen = 0;
		
		for(int i=0; i<array.length; i++)
		{
			for(int j=0; j<array.length; j++)
			{
				int n = array.length;
				countGreen = array[i][j] + array[i][Math.floorMod(j-1, n)] + array[Math.floorMod(i+1, n)][Math.floorMod(j-1, n)] + array[Math.floorMod(i-1, n)][j] + array[Math.floorMod(i+1, n)][j] + array[Math.floorMod(i-1, n)][Math.floorMod(j+1, n)] + array[i][Math.floorMod(j+1, n)];
				if (countGreen == 0 || countGreen == 1 || countGreen == 2)
				{
					//Change to Green
					countGreenArray[i][j] = countGreen;
					newArray[i][j] = 1;
				}
				else if (countGreen == 3)
				{
					//Keep
					countGreenArray[i][j] = countGreen;
				}
				else
				{
					//Change to Black;
					countGreenArray[i][j] = countGreen;
					newArray[i][j] = 0;
				}
				countGreen=0;
			}
		}
		
		System.out.println("Number of Greens");
		//Loop through entire outer loop
		for(int i=0; i<countGreenArray.length; i++)
		{
			//Loop through entire inner loop
			for(int j=0; j<countGreenArray[i].length; j++)
			{
				//Creates spacing between numbers 
				System.out.print(countGreenArray[i][j] + "  ");
			}	
			System.out.println();
		}
		System.out.println();
		
		System.out.println("Transformed");
		//Loop through entire outer loop
		for(int i=0; i<newArray.length; i++)
		{
			//Loop through entire inner loop
			for(int j=0; j<newArray[i].length; j++)
			{
				//Creates spacing between numbers 
				//System.out.print(newArray[i][j] + "  ");
				if(newArray[i][j] == 1)
				{
					System.out.print(ANSI_GREEN + newArray[i][j] + "  " + ANSI_RESET);
				}
				else
				{
					System.out.print(ANSI_BLACK + newArray[i][j] + "  " + ANSI_RESET);
				}
			}	
			System.out.println();
		}
		System.out.println();
	}
}
