import java.util.Random;

public class LizardCAGenerator 
{
	static int [][] newArrayMiddle = new int[20][20];
	
	public static void checkForGreenMiddle(int[][] array)
	{
		//Counter to count the number of greens
		int countGreen = 0;
		
		//Create new array to transfer information
		  
		
		//Duplicate Array
		for(int i=0; i<array.length; i++)
		{
			newArrayMiddle[i] = array[i].clone();
		}
		
		//Start at i=1 and j=1 because i-1 and j-1 is out of bounds
		for(int i=1; i<array.length-1; i++)
		{
			for(int j=1; j<array.length-1; j++)
			{
				//Count the number of Greens (1)
				
				//Check center
				if(array[i][j] == 1)
				{
					countGreen++;
				}
				else
				{
					countGreen = countGreen + 0;
				}
				
				//Check Left Neighbor
				if(array[i][j-1] == 1)
				{
					countGreen++;
				}
				else
				{
					countGreen = countGreen + 0;
				}
				
				//Check Right Neighbor
				if(array[i][j+1] == 1)
				{
					countGreen++;
				}
				else
				{
					countGreen = countGreen + 0;
				}
				
				//Check Left Up Neighbor
				if(array[i-1][j] == 1)
				{
					countGreen++;
				}
				else
				{
					countGreen = countGreen + 0;
				}
				
				//Check Right Up Neighbor
				if(array[i-1][j+1] == 1)
				{
					countGreen++;
				}
				else
				{
					countGreen = countGreen + 0;
				}
				
				//Check Left Bottom Neighbor
				if(array[i+1][j-1] == 1)
				{
					countGreen++;
				}
				else
				{
					countGreen = countGreen + 0;
				}
				
				//Check Right Bottom Neighbor
				if(array[i+1][j] == 1)
				{
					countGreen++;
				}
				else
				{
					countGreen = countGreen + 0;
				}
				
				//Line Spacing
				//System.out.print(" ");
				
				//If there is less than 3 greens then add green
				if(countGreen<3)
				{
					//Check center
					if(array[i][j] == 0)
					{
						newArrayMiddle[i][j] = 1;
						countGreen++;
					}
					else
					{
						newArrayMiddle[i][j] = 1;
					}
				}
				
				if(countGreen<3)
				{
					//Check Left Neighbor
					if(array[i][j-1] == 0)
					{
						newArrayMiddle[i][j-1] = 1;
						countGreen++;
					}			
					else
					{
						newArrayMiddle[i][j-1] = 1;
					}
				}
				
				if(countGreen<3)
				{
					//Check Right Neighbor
					if(array[i][j+1] == 0)
					{							
						newArrayMiddle[i][j+1] = 1;
						countGreen++;
					}
					else
					{
						newArrayMiddle[i][j+1] = 1;
					}
				}
					
				if(countGreen<3)
				{
					//Check Left Up Neighbor
					if(array[i-1][j] == 0)						
					{
						newArrayMiddle[i-1][j] = 1;
						countGreen++;
					}
					else
					{
						newArrayMiddle[i-1][j] = 1;
					}
				}
				
				if(countGreen<3)
				{
					//Check Right Up Neighbor
					if(array[i-1][j+1] == 0)
					{
						newArrayMiddle[i-1][j+1] = 1;
						countGreen++;
					}
					else
					{
						newArrayMiddle[i-1][j+1] = 1;
					}
				}

				if(countGreen<3)
				{
					//Check Left Bottom Neighbor
					if(array[i+1][j-1] == 0)
					{
						newArrayMiddle[i+1][j-1] = 1;
						countGreen++;
					}
					else
					{
						newArrayMiddle[i+1][j-1] = 1;
					}
				}
					
				if(countGreen<3)
				{
					//Check Right Bottom Neighbor
					if(array[i+1][j] == 0)
					{
						newArrayMiddle[i+1][j] = 1;
						countGreen++;
					}
					else
					{
						newArrayMiddle[i+1][j] = 1;
					}
				}
					
				//If there is more than 3 greens then change to black
				if(countGreen>3)
				{
					//Check center
					if(array[i][j] == 1)
					{
						newArrayMiddle[i][j] = 0;
						countGreen--;
					}
					else
					{
						newArrayMiddle[i][j] = 0;
					}
				}
					
				if(countGreen>3)
				{
					//Check Left Neighbor
					if(array[i][j-1] == 1)
					{
						newArrayMiddle[i][j-1] = 0;
						countGreen--;
					}	
					else
					{
						newArrayMiddle[i][j-1] = 0;
					}
				}
					
				if(countGreen>3)
				{
					//Check Right Neighbor
					if(array[i][j+1] == 1)
					{							
						newArrayMiddle[i][j+1] = 0;
						countGreen--;
					}
					else
					{
						newArrayMiddle[i][j+1] = 0;
					}
				}
					
				if(countGreen>3)
				{
					//Check Left Up Neighbor
					if(array[i-1][j] == 1)						
					{
						newArrayMiddle[i-1][j] = 0;
						countGreen--;
					}
					else
					{
						newArrayMiddle[i-1][j] = 0;
					}
				}
				
				if(countGreen>3)
				{
					//Check Right Up Neighbor
					if(array[i-1][j+1] == 1)
					{
						newArrayMiddle[i-1][j+1] = 0;
						countGreen--;
					}
					else
					{
						newArrayMiddle[i-1][j+1] = 0;
					}
				}

				if(countGreen>3)
				{
					//Check Left Bottom Neighbor
					if(array[i+1][j-1] == 1)
					{
						newArrayMiddle[i+1][j-1] = 0;
						countGreen--;
					}
					else
					{
						newArrayMiddle[i+1][j-1] = 0;
					}
				}
					
				if(countGreen>3)
				{
					//Check Right Bottom Neighbor
					if(array[i+1][j] == 1)
					{
						newArrayMiddle[i+1][j] = 0;
						countGreen--;
					}
					else
					{
						newArrayMiddle[i+1][j] = 0;
					}
				}		
				countGreen = 0;
			}
		}
		
		System.out.println("Center Transformation");
		//Loop through entire outer loop
		for(int i=0; i<newArrayMiddle.length; i++)
		{
			//Loop through entire inner loop
			for(int j=0; j<newArrayMiddle[i].length; j++)
			{
				//Creates spacing between numbers 
				System.out.print(newArrayMiddle[i][j] + "  ");
			}	
			System.out.println();
		}
		System.out.println();
	}
	
	static int [][] newArrayBorder = new int[20][20];
	
	public static void checkForGreenBorderLeft(int[][] newArrayMiddle)
	{
		int countGreen = 0;
		
		//Duplicate Array
		for(int i=0; i<newArrayMiddle.length; i++)
		{
			newArrayBorder[i] = newArrayMiddle[i].clone();
		}
		
		//Start Left Border
		for(int i=1; i<newArrayMiddle.length-1; i++)
		{
			//Count the number of Greens (1)
			int j=0;
					
			//Check Center
			if(newArrayMiddle[i][j] == 1)
			{
				countGreen++;
			}
			else
			{
				countGreen = countGreen + 0;				
			}
					
			//Check Left Neighbor
			if(newArrayMiddle[i][j+19] == 1)
			{
				countGreen++;
			}
			else
			{
				countGreen = countGreen + 0;
			}
					
			//Check Right Neighbor
			if(newArrayMiddle[i][j+1] == 1)
			{
				countGreen++;
			}
			else
			{
				countGreen = countGreen + 0;
			}
					
			//Check Left Up Neighbor
			if(newArrayMiddle[i-1][j] == 1)
			{
				countGreen++;
			}
			else
			{
				countGreen = countGreen + 0;
			}
					
			//Check Right Up Neighbor
			if(newArrayMiddle[i-1][j+1] == 1)
			{
				countGreen++;
			}
			else
			{
				countGreen = countGreen + 0;
			}
					
			//Check Left Bottom Neighbor
			if(newArrayMiddle[i+1][j+19] == 1)
			{
				countGreen++;
			}
			else
			{
				countGreen = countGreen + 0;
			}
					
			//Check Right Bottom Neighbor
			if(newArrayMiddle[i+1][j] == 1)
			{
				countGreen++;
			}
			else
			{
				countGreen = countGreen + 0;
			}
					
			//If there is less than 3 greens then add green
			if(countGreen<3)
			{
				//Check center
				if(newArrayMiddle[i][j] == 0)
				{
					newArrayBorder[i][j] = 1;
					countGreen++;
				}
			}
			
			if(countGreen<3)
			{
				//Check Left Neighbor
				if(newArrayMiddle[i][j+19] == 0)
				{
					newArrayBorder[i][j+19] = 1;
					countGreen++;
				}					
			}
			
			if(countGreen<3)
			{
				//Check Right Neighbor
				if(newArrayMiddle[i][j+1] == 0)
				{							
					newArrayBorder[i][j+1] = 1;
					countGreen++;
				}
			}
				
			if(countGreen<3)
			{
				//Check Left Up Neighbor
				if(newArrayMiddle[i-1][j] == 0)						
				{
					newArrayBorder[i-1][j] = 1;
					countGreen++;
				}
			}
			
			if(countGreen<3)
			{
				//Check Right Up Neighbor
				if(newArrayMiddle[i-1][j+1] == 0)
				{
					newArrayBorder[i-1][j+1] = 1;
					countGreen++;
				}
			}

			if(countGreen<3)
			{
				//Check Left Bottom Neighbor
				if(newArrayMiddle[i+1][j+19] == 0)
				{
					newArrayBorder[i+1][j+19] = 1;
					countGreen++;
				}
			}
				
			if(countGreen<3)
			{
				//Check Right Bottom Neighbor
				if(newArrayMiddle[i+1][j] == 0)
				{
					newArrayBorder[i+1][j] = 1;
					countGreen++;
				}
			}
			
			//If there is more than 3 greens then change to black
			if(countGreen>3)
			{
				//Check center
				if(newArrayMiddle[i][j] == 1)
				{
					newArrayBorder[i][j] = 0;
					countGreen--;
				}
			}
						
			if(countGreen>3)
			{
				//Check Left Neighbor
				if(newArrayMiddle[i][j+19] == 1)
				{
					newArrayBorder[i][j+19] = 0;
					countGreen--;
				}					
			}
						
			if(countGreen>3)
			{
				//Check Right Neighbor
				if(newArrayMiddle[i][j+1] == 1)
				{							
					newArrayBorder[i][j+1] = 0;
					countGreen--;
				}
			}
						
			if(countGreen>3)
			{
				//Check Left Up Neighbor
				if(newArrayMiddle[i-1][j] == 1)						
				{
					newArrayBorder[i-1][j] = 0;
					countGreen--;
				}
			}
					
			if(countGreen>3)
			{
				//Check Right Up Neighbor
				if(newArrayMiddle[i-1][j+1] == 1)
				{
					newArrayBorder[i-1][j+1] = 0;
					countGreen--;
				}
			}

			if(countGreen>3)
			{
				//Check Left Bottom Neighbor
				if(newArrayMiddle[i+1][j+19] == 1)
				{
					newArrayBorder[i+1][j+19] = 0;
					countGreen--;
				}
			}
						
			if(countGreen>3)
			{
				//Check Right Bottom Neighbor
				if(newArrayMiddle[i+1][j] == 1)
				{
					newArrayBorder[i+1][j] = 0;
					countGreen--;
				}
			}
			countGreen = 0;
		}
	
	System.out.println("Left Border Transformation");
	//Loop through entire outer loop
	for(int i=0; i<newArrayBorder.length; i++)
	{
		//Loop through entire inner loop
		for(int j=0; j<newArrayBorder[i].length; j++)
		{
			System.out.print(newArrayBorder[i][j] + "  ");
		}	
		System.out.println();
	}
}
	
	static int [][] newArrayBorderRight = new int[20][20];
	
	public static void checkForGreenBorderRight(int[][] newArrayBorder)
	{
		int countGreen = 0;
		
		//Duplicate Array
		for(int i=0; i<newArrayBorder.length; i++)
		{
			newArrayBorderRight[i] = newArrayBorder[i].clone();
		}
		
		//Start Left Border
		for(int i=1; i<newArrayBorderRight.length-1; i++)
		{
			//Count the number of Greens (1)
			int j=19;
					
			//Check Center
			if(newArrayBorder[i][j] == 1)
			{
				countGreen++;
			}
			else
			{
				countGreen = countGreen + 0;				
			}
					
			//Check Left Neighbor
			if(newArrayBorder[i][j-1] == 1)
			{
				countGreen++;
			}
			else
			{
				countGreen = countGreen + 0;
			}
					
			//Check Right Neighbor
			if(newArrayBorder[i][0] == 1)
			{
				countGreen++;
			}
			else
			{
				countGreen = countGreen + 0;
			}
					
			//Check Left Up Neighbor
			if(newArrayBorder[i-1][j] == 1)
			{
				countGreen++;
			}
			else
			{
				countGreen = countGreen + 0;
			}
					
			//Check Right Up Neighbor
			if(newArrayBorder[i-1][0] == 1)
			{
				countGreen++;
			}
			else
			{
				countGreen = countGreen + 0;
			}
					
			//Check Left Bottom Neighbor
			if(newArrayBorder[i+1][j-1] == 1)
			{
				countGreen++;
			}
			else
			{
				countGreen = countGreen + 0;
			}
					
			//Check Right Bottom Neighbor
			if(newArrayBorder[i+1][j] == 1)
			{
				countGreen++;
			}
			else
			{
				countGreen = countGreen + 0;
			}
					
			//If there is less than 3 greens then add green
			if(countGreen<3)
			{
				//Check center
				if(newArrayBorder[i][j] == 0)
				{
					newArrayBorderRight[i][j] = 1;
					countGreen++;
				}
			}
			
			if(countGreen<3)
			{
				//Check Left Neighbor
				if(newArrayBorder[i][j-1] == 0)
				{
					newArrayBorderRight[i][j-1] = 1;
					countGreen++;
				}					
			}
			
			if(countGreen<3)
			{
				//Check Right Neighbor
				if(newArrayBorder[i][0] == 0)
				{							
					newArrayBorderRight[i][0] = 1;
					countGreen++;
				}
			}
				
			if(countGreen<3)
			{
				//Check Left Up Neighbor
				if(newArrayBorder[i-1][j] == 0)						
				{
					newArrayBorderRight[i-1][j] = 1;
					countGreen++;
				}
			}
			
			if(countGreen<3)
			{
				//Check Right Up Neighbor
				if(newArrayBorder[i-1][0] == 0)
				{
					newArrayBorderRight[i-1][0] = 1;
					countGreen++;
				}
			}

			if(countGreen<3)
			{
				//Check Left Bottom Neighbor
				if(newArrayBorder[i+1][j-1] == 0)
				{
					newArrayBorderRight[i+1][j-1] = 1;
					countGreen++;
				}
			}
				
			if(countGreen<3)
			{
				//Check Right Bottom Neighbor
				if(newArrayBorder[i+1][j] == 0)
				{
					newArrayBorderRight[i+1][j] = 1;
					countGreen++;
				}
			}
			
			//If there is more than 3 greens then change to black
			if(countGreen>3)
			{
				//Check center
				if(newArrayBorder[i][j] == 1)
				{
					newArrayBorderRight[i][j] = 0;
					countGreen--;
				}
			}
						
			if(countGreen>3)
			{
				//Check Left Neighbor
				if(newArrayBorder[i][j-1] == 1)
				{
					newArrayBorderRight[i][j-1] = 0;
					countGreen--;
				}					
			}
						
			if(countGreen>3)
			{
				//Check Right Neighbor
				if(newArrayBorder[i][0] == 1)
				{							
					newArrayBorderRight[i][0] = 0;
					countGreen--;
				}
			}
						
			if(countGreen>3)
			{
				//Check Left Up Neighbor
				if(newArrayBorder[i-1][j] == 1)						
				{
					newArrayBorderRight[i-1][j] = 0;
					countGreen--;
				}
			}
					
			if(countGreen>3)
			{
				//Check Right Up Neighbor
				if(newArrayBorder[i-1][0] == 1)
				{
					newArrayBorderRight[i-1][0] = 0;
					countGreen--;
				}
			}

			if(countGreen>3)
			{
				//Check Left Bottom Neighbor
				if(newArrayBorder[i+1][j-1] == 1)
				{
					newArrayBorderRight[i+1][j-1] = 0;
					countGreen--;
				}
			}
						
			if(countGreen>3)
			{
				//Check Right Bottom Neighbor
				if(newArrayBorder[i+1][j] == 1)
				{
					newArrayBorderRight[i+1][j] = 0;
					countGreen--;
				}
			}
			countGreen = 0;
		}
		
	System.out.println();
	System.out.println("Right Border Transformation");
	//Loop through entire outer loop
	for(int i=0; i<newArrayBorder.length; i++)
	{
		//Loop through entire inner loop
		for(int j=0; j<newArrayBorder[i].length; j++)
		{
			System.out.print(newArrayBorder[i][j] + "  ");
		}	
		System.out.println();
	}
}
	
	static int [][] newArrayBorderTop = new int[20][20];
	
	public static void checkForGreenBorderTop(int[][] newArrayBorderRight)
	{
		int countGreen = 0;
		
		//Duplicate Array
		for(int i=0; i<newArrayBorderTop.length; i++)
		{
			newArrayBorderTop[i] = newArrayBorderRight[i].clone();
		}
		
		
		//Start Left Border
		for(int j=1; j<newArrayBorderRight.length-1; j++)
		{
			//Count the number of Greens (1)
			int i=0;
					
			//Check Center
			if(newArrayBorderRight[i][j] == 1)
			{
				countGreen++;
			}
			else
			{
				countGreen = countGreen + 0;				
			}
					
			//Check Left Neighbor
			if(newArrayBorder[i][j-1] == 1)
			{
				countGreen++;
			}
			else
			{
				countGreen = countGreen + 0;
			}
					
			//Check Right Neighbor
			if(newArrayBorder[i][j+1] == 1)
			{
				countGreen++;
			}
			else
			{
				countGreen = countGreen + 0;
			}
					
			//Check Left Up Neighbor
			if(newArrayBorder[19][j] == 1)
			{
				countGreen++;
			}
			else
			{
				countGreen = countGreen + 0;
			}
					
			//Check Right Up Neighbor
			if(newArrayBorder[19][j+1] == 1)
			{
				countGreen++;
			}
			else
			{
				countGreen = countGreen + 0;
			}
					
			//Check Left Bottom Neighbor
			if(newArrayBorder[i+1][j-1] == 1)
			{
				countGreen++;
			}
			else
			{
				countGreen = countGreen + 0;
			}
					
			//Check Right Bottom Neighbor
			if(newArrayBorder[i+1][j] == 1)
			{
				countGreen++;
			}
			else
			{
				countGreen = countGreen + 0;
			}
					
			//If there is less than 3 greens then add green
			if(countGreen<3)
			{
				//Check center
				if(newArrayBorder[i][j] == 0)
				{
					newArrayBorderTop[i][j] = 1;
					countGreen++;
				}
			}
			
			if(countGreen<3)
			{
				//Check Left Neighbor
				if(newArrayBorder[i][j-1] == 0)
				{
					newArrayBorderTop[i][j-1] = 1;
					countGreen++;
				}					
			}
			
			if(countGreen<3)
			{
				//Check Right Neighbor
				if(newArrayBorder[i][j+1] == 0)
				{							
					newArrayBorderTop[i][j+1] = 1;
					countGreen++;
				}
			}
				
			if(countGreen<3)
			{
				//Check Left Up Neighbor
				if(newArrayBorder[19][j] == 0)						
				{
					newArrayBorderTop[19][j] = 1;
					countGreen++;
				}
			}
			
			if(countGreen<3)
			{
				//Check Right Up Neighbor
				if(newArrayBorder[19][j+1] == 0)
				{
					newArrayBorderTop[19][j+1] = 1;
					countGreen++;
				}
			}

			if(countGreen<3)
			{
				//Check Left Bottom Neighbor
				if(newArrayBorder[i+1][j-1] == 0)
				{
					newArrayBorderTop[i+1][j-1] = 1;
					countGreen++;
				}
			}
				
			if(countGreen<3)
			{
				//Check Right Bottom Neighbor
				if(newArrayBorder[i+1][j] == 0)
				{
					newArrayBorderTop[i+1][j] = 1;
					countGreen++;
				}
			}
			
			//If there is more than 3 greens then change to black
			if(countGreen>3)
			{
				//Check center
				if(newArrayBorder[i][j] == 1)
				{
					newArrayBorderTop[i][j] = 0;
					countGreen--;
				}
			}
						
			if(countGreen>3)
			{
				//Check Left Neighbor
				if(newArrayBorder[i][j-1] == 1)
				{
					newArrayBorderTop[i][j-1] = 0;
					countGreen--;
				}					
			}
						
			if(countGreen>3)
			{
				//Check Right Neighbor
				if(newArrayBorder[i][j+1] == 1)
				{							
					newArrayBorderTop[i][j+1] = 0;
					countGreen--;
				}
			}
						
			if(countGreen>3)
			{
				//Check Left Up Neighbor
				if(newArrayBorder[19][j] == 1)						
				{
					newArrayBorderTop[19][j] = 0;
					countGreen--;
				}
			}
					
			if(countGreen>3)
			{
				//Check Right Up Neighbor
				if(newArrayBorder[19][j+1] == 1)
				{
					newArrayBorderTop[19][j+1] = 0;
					countGreen--;
				}
			}

			if(countGreen>3)
			{
				//Check Left Bottom Neighbor
				if(newArrayBorder[i+1][j-1] == 1)
				{
					newArrayBorderTop[i+1][j-1] = 0;
					countGreen--;
				}
			}
						
			if(countGreen>3)
			{
				//Check Right Bottom Neighbor
				if(newArrayBorder[i+1][j] == 1)
				{
					newArrayBorderTop[i+1][j] = 0;
					countGreen--;
				}
			}
			countGreen = 0;
		}
		
	System.out.println();
	System.out.println("Top Border Transformation");
	//Loop through entire outer loop
	for(int i=0; i<newArrayBorderTop.length; i++)
	{
		//Loop through entire inner loop
		for(int j=0; j<newArrayBorderTop[i].length; j++)
		{
			System.out.print(newArrayBorderTop[i][j] + "  ");
		}	
		System.out.println();
	}
}
	
	public static void main(String[] args)
	{
		//Create a 20x20 array
		int[][] array = new int[20][20];
		
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
		
		checkForGreenMiddle(array);
		checkForGreenBorderLeft(newArrayMiddle);
		checkForGreenBorderRight(newArrayBorder);
		checkForGreenBorderTop(newArrayBorderRight);
	}
}
