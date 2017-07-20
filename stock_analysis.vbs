Sub stock_analysis()

Dim total As Double
Dim i As Long
Dim change As Single
Dim j As Integer
Dim start As Long
Dim rowCount As Long
Dim percentChange As Single
Dim days As Integer
Dim dailyChange As Single
Dim averageChange As Single

'Dim ws1 As Worksheet
Dim ws2 As Worksheet

' results can be changed to whatever worksheet is needed
Set ws2 = Worksheets("Results")

' Set Headers
ws2.Cells(1,1).Value = "Ticker"
ws2.Cells(1,2).Value = "Total Change"
ws2.Cells(1,3).Value = "% Change"
ws2.Cells(1,4).Value = "Avg. Daily Change"
ws2.Cells(1,5).Value = "Volume"

' Greatest results
ws2.Cells(2,7).Value = "Greatest Volume"
ws2.Cells(5,7).Value = "Greatest % Increase"
ws2.Cells(8,7).Value = "Greatest % Decrease"
ws2.Cells(11,7).Value = "Greatest Avg. Change"

' Set initial values
j = 0
total = 0
change = 0
start = 2
dailyChange = 0

' get the row number of the last row with data
rowCount = Cells(Rows.Count, "A").End(xlUp).Row

' 701937 and 78
For i = 2 To rowCount
    If Cells(i + 1, 1).Value <> Cells(i, 1).Value Then

    ' additional code goes here

    End If
Next i

If Cells(i + 1, 1).Value <> Cells(i, 1).Value Then
     '...
     ' reset variables for new stock ticker
     total = 0
     change = 0
     j = j + 1
     days = 0
     dailyChange = 0
 Else
     total = total + Cells(i, 7).Value
     change = change + (Cells(i, 6) - Cells(i, 3))
     ' change in high and low
     dailyChange = dailyChange + (Cells(i, 4) - Cells(i, 5))

 ' take the max and min and place them in a separate part in the worksheet
ws2.Cells(2, 8) = WorksheetFunction.Max(ws2.Range("E2:E" & rowCount))
ws2.Cells(5, 8) = "%" & WorksheetFunction.Max(ws2.Range("C2:C" & rowCount)) * 100
ws2.Cells(8, 8) = "%" & WorksheetFunction.Min(ws2.Range("C2:C" & rowCount)) * 100
ws2.Cells(11, 8) = WorksheetFunction.Max(ws2.Range("D2:D" & rowCount))