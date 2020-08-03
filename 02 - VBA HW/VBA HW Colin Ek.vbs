Attribute VB_Name = "Module1"
Sub VBA_HW():
On Error Resume Next
    'Step 1: Create variables and set to zero, where appropriate
    Dim Ticker As String 'Need string Type
    Dim Yearly_Change As Integer
    Yearly_Change = 0
    Dim Percent_Change As Integer
    Percent_Change = 0
    Dim Total_Stock_Volume As Variant
    Total_Stock_Volume = 0
    Dim First As Variant
    First = 0
    Dim Last As Variant
    First = 0
    Dim FirstP As Variant
    First = 0
    Dim LastP As Variant
    First = 0
    
    'Step 2: Set Headers
    Range("I1").Value = "Ticker"
    Range("J1").Value = "Yearly_Change"
    Range("K1").Value = "Percent_Change"
    Range("L1").Value = "Total_Stock_Volume"
    Range("P1").Value = "Ticker"
    Range("Q1").Value = "Value"
    
    'Step x: Counts the number of rows
    lastrow = Cells(Rows.Count, 1).End(xlUp).Row
    
    ' Keep track of the location for each credit card brand in the summary table
    Dim Summary_Table_Row As Integer
    Summary_Table_Row = 2
    
    ' Loop through all values
  For i = 2 To lastrow

    If Cells(i - 1, 1).Value <> Cells(i, 1).Value Then
    
          First = Cells(i, 3).Value
          FirstP = Cells(i, 3).Value / 100
          
      ElseIf Cells(i + 1, 1).Value <> Cells(i, 1).Value Then
      
        ' Set values for Ticker and Last
        Ticker = Cells(i, 1).Value
        Last = Cells(i, 6).Value
        LastP = Cells(i, 6).Value / 100
        
        ' Add to the Total_Stock_Volume
        Total_Stock_Volume = Total_Stock_Volume + Cells(i, 7).Value
        
        ' Print the Brand Amount to the Summary Table
        Range("I" & Summary_Table_Row).Value = Ticker
        Range("L" & Summary_Table_Row).Value = Total_Stock_Volume
        Range("J" & Summary_Table_Row).Value = Last - First
        Range("K" & Summary_Table_Row).NumberFormat = "0.00%"
        
        If FirstP <> 0 And LastP <> 0 Then:
        
            Range("K" & Summary_Table_Row).Value = (LastP - FirstP) / FirstP
        
        ' Add one row to the Summary Table
        Summary_Table_Row = Summary_Table_Row + 1
            
        ' Reset the Total_Stock_Volume variable for next comparison
         Total_Stock_Volume = 0

      Else

      ' When Ticker values are the same, grab value and add to Total_Stock_Volume
      Total_Stock_Volume = Total_Stock_Volume + Cells(i, 7).Value
      
    End If

  Next i

'Conditional Formatting for Color
  For i = 2 To lastrow

        If Cells(i, 10).Value > 0 Then
            Cells(i, 10).Interior.ColorIndex = 4
        ElseIf Cells(i, 10).Value <= 0 Then
            Cells(i, 10).Interior.ColorIndex = 3
                
    End If

  Next i

'Challenge Tasks
Dim Max_Name As String
Dim Max As Variant
Max = 0
Dim Min_Name As String
Dim Min As Variant
Min = 0
Dim GTV_Name As String
Dim GTV As Variant
GTV = 0

Cells(2, 15).Value = "Greatest % Increase"
Cells(3, 15).Value = "Greatest % Decrease"
Cells(4, 15).Value = "Greatest Total Volume"

Cells(2, 17).NumberFormat = "0.00%"
Cells(3, 17).NumberFormat = "0.00%"

'Max
For i = 2 To lastrow
    If Cells(i, 11).Value > Max Then
        Max = Cells(i, 11).Value
        Max_Name = Cells(i, 9).Value
        Cells(2, 16).Value = Max_Name
        Cells(2, 17).Value = Max
    End If
Next i

'Min
For i = 2 To lastrow
    If Cells(i, 11).Value < Min Then
        Min = Cells(i, 11).Value
        Min_Name = Cells(i, 9).Value
        Cells(3, 16).Value = Min_Name
        Cells(3, 17).Value = Min
    End If

Next i
  
'Greatest Total Volume
For i = 2 To lastrow
    If Cells(i, 12).Value > GTV Then
        GTV = Cells(i, 12).Value
        GTV_Name = Cells(i, 9).Value
        Cells(4, 16).Value = GTV_Name
        Cells(4, 17).Value = GTV

    End If

Next i

End Sub






























