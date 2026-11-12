---
title: "Using Basic Search Syntax Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "API_GB/Using_Basic_Search_Syntax_Example_VBNET.htm"
---

# Using Basic Search Syntax Example (VB.NET)

This example shows how to search the vault for file and folder card variables using CreateSearch2 search syntax.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
'----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Start Microsoft Visual Studio.
 '    a. Click File > New > Project > Visual Basic > Console Application.
 '    b. Type Search_VBNET in Name.
 '    c. Click Browse and navigate to the folder where to create the project.
 '    d. Click OK.
 '    e. Click Show All Files in the Solution Explorer toolbar and expand
 '       Module1.vb in the Solution Explorer.
 '    f. Replace all the code for Module1.vb with this code.
 ' 2. Add EPDM.Interop.epdm.dll as a reference (right-click the project
 '    name in the Solution Explorer, click Add Reference, click
 '     Assemblies > Framework in the left-side panel, browse to the top folder of
 '    your SOLIDWORKS PDM Professional installation, locate and select
 '     EPDM.Interop.epdm.dll, click Open, click Add, and click Close).
 ' 3. Change the vault name and the vault view path in the code.
' 4. Make sure your vault contains a text file data card with a Document Number data card variable,
'    and checked-in files with data card values exactly as described in the code.
 ' 5. Click Debug > Start Debugging or press F5.
 '
 ' Postconditions: Press a key when prompted in the console.
 '---------------------------------------------------------------------------
 'Module1.vb
 Imports System
 Imports System.Collections.Generic
 Imports System.Linq
 Imports System.Text
 Imports System.Threading.Tasks
 Imports EPDM.Interop.epdm
 Module   Module1

       Sub Main(ByVal args  As   String())
           Console.WriteLine("Press a key...")
           Console.ReadKey()
            Dim CurrentVault  As IEdmVault21 =   TryCast(New EdmVault5(), IEdmVault21)
           CurrentVault.LoginAuto("JEB5", 0)

            ' The vault contains these files        The file data cards contain these variables And values:
            ' DocNum=five-six-seven Comnt=ijk.txt   @Document Number=567 & @Comment=ijk
            ' DocNum=five-six-seven Comnt=xyz.txt   @Document Number=567 & @Comment=xyz
            ' DocNum=one-two-three Comnt=abc.txt    @Document Number=123 & @Comment=abc

            Dim _searchResult  As IEdmSearchResult5
            Dim _search  As IEdmSearch9 =   CType(CurrentVault.CreateSearch2(), IEdmSearch9)
            Dim VarNames0  As   String() = {}
           _search.AddMultiVariableCondition(VarNames0,   "@:")  ' poVariableNames can be Nothing
           _search.GetFirstResult()
            Dim OriginatedFromCreateSearch2  As   Boolean = _search.GetSyntaxErrors()  IsNot  Nothing
           Console.WriteLine("OriginatedFromCreateSearch2  = " & OriginatedFromCreateSearch2)
           Console.WriteLine("Press a key...")
           Console.ReadKey()

            For i  As  Integer = 0  To 7 - 1
               Dim ExceptionEncountered  As   Boolean =   False
              _search.Clear()
              _search.StartFolderID = CurrentVault.GetFolderFromPath("C:\Users\J4M\Desktop\JEB5").ID

               Select  Case i
                   Case 0  ' Single variable search conditions with special criteria and variables
                      Console.WriteLine("")
                      Console.WriteLine("Single variable search conditions with special criteria and variables:")
                      _search.FileName =   "(limit | cam) !wheel OR DocNum"
                      _search.AddVariable2("Document Number",  "56 & 7")
                      _search.AddVariable2("Comment",   "xy | z NOT a")
                       ' Finds DocNum=five-six-seven Comnt=xyz.txt
                   Case 1  ' Multi-variable condition with extended search name syntax
                      Console.WriteLine("")
                      Console.WriteLine("Multi-variable condition with extended search name syntax:")
                       ' VarNames array declares that all elements are strings
                        Dim VarNames  As   String() = {"""Document Number""",  "Comment",  "51",   "_Name"}
                       ' Both xy And z must be in the same card variable - owing to {}
                       ' Text 567 can be in a different card variable
                       ' : turns on multi-value search logic
                      _search.AddMultiVariableCondition(VarNames,   ":567 {z xy}")
                       ' Finds DocNum=five-six-seven Comnt=xyz.txt
                   Case 2  ' Multi-variable condition searches all the card variables in file/folder name
                      Console.WriteLine("")
                      Console.WriteLine("Multi-variable condition for all the vault variables:")
                       ' Unquoted _Name represents file/folder name
                       ' "" or 0 represents any card variable
                        Dim VarNames  As   String() = {"""""",   "_Name"}
                      _search.AddMultiVariableCondition(VarNames,   ":567 xyz | five xy")
                       ' Finds DocNum=five-six-seven Comnt=xyz.txt
                   Case 3  ' Extended multi-variable condition with erroneously unquoted card variable names
                      Console.WriteLine("")
                      Console.WriteLine("Multi-variable condition with erroneously unquoted names:")
                        Try
                            Dim VarNames  As   String() = {"Document Number",  "Comment",  "Project Name"}
                          _search.AddMultiVariableCondition(VarNames,   ":567 xyz | five xy")
                           ' Causes an exception because there are card variable names with spaces that need extra quotation marks
                        Catch ex  As System.ArgumentException
                          Console.WriteLine("Wrong variable syntax... HRESULT = 0x" & ex.HResult.ToString("X") & ex.Message)
                          ExceptionEncountered =   True
                      End  Try
                   Case 4   ' Syntax errors are not displayed; no documents returned
                      Console.WriteLine("")
                      Console.WriteLine("Syntax errors, but not displayed:")
                      _search.FileName =   "(limit = | cam) !wheel OR AND DocNum"
                      _search.AddVariable2("Document Number",  "56 && 7")
                      _search.AddVariable2("Comment",   "xy | z() NOT a")
                   Case 5  ' Syntax errors displayed (because @: is at the beginning of a condition); no documents returned
                      Console.WriteLine("")
                      Console.WriteLine("Syntax errors:")
                      _search.FileName =   "@:(limit = | cam) !wheel OR AND DocNum"
                      _search.AddVariable2("Document Number",  "56 && 7")
                      _search.AddVariable2("Comment",   "@:xy | z() NOT a")
                   Case 6   ' Multi-value syntax with error reporting (because @: is at the beginning of a condition)
                      Console.WriteLine("")
                      Console.WriteLine("Advanced search syntax:")
                       ' The first argument can be Nothing because all the card variables are defined with variable binding specifiers (@) inside the second argument which is the condition
                       ' The second argument uses the advanced specifier which allows variable bindings
                       ' The second argument specifies to look for files that have (Comment = abc and any card variables with xyz) OR (a file name or "Document Number" that contains 123 or ab, but not five)
                       '
                       ' Finds DocNum=one-two-three Comnt=abc.txt
                      _search.AddMultiVariableCondition(VarNames0,   "@: @Comment=abc & @""""(xyz) | @(""Document Number"" | _Name)(123 ab & !five)")

               End  Select

               If ExceptionEncountered   Then
                  _searchResult =   Nothing
               Else
                  _searchResult = _search.GetFirstResult()
               End  If

               If _searchResult  Is   Nothing   Then
                  Console.WriteLine("Returned null...")
               Else
                  Console.WriteLine("Returned a file list...")
               End  If

              Console.WriteLine("Press a key...")
              Console.ReadKey()

               If _searchResult   IsNot   Nothing   Then

                   While _searchResult   IsNot   Nothing
                      Console.WriteLine("NAME = " & _searchResult.Name   ", PATH = " + _searchResult.Path)
                      Console.WriteLine("Press a key...")
                      Console.ReadKey()
                      _searchResult = _search.GetNextResult()
                   End  While
               Else
                   Dim SyntaxErrors  As   String() = _search.GetSyntaxErrors()

                   If SyntaxErrors   IsNot   Nothing   Then

                        For   Each s  As   String  In SyntaxErrors
                          Console.WriteLine(s)
                          Console.WriteLine("Press a key...")
                          Console.ReadKey()
                        Next
                  End  If
               End  If
            Next
       End  Sub

 End  Module
```

```
Back to top
```
