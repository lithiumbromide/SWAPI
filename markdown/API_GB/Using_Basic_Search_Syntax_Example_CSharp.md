---
title: "Using Basic Search Syntax Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "API_GB/Using_Basic_Search_Syntax_Example_CSharp.htm"
---

# Using Basic Search Syntax Example (C#)

This example shows how to search the vault for file and folder card variables using CreateSearch2 search syntax.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Start Microsoft Visual Studio.
 //    a. Click File > New > Project > Visual C# > Console Application.
 //    b. Type Search in Name.
 //    c. Click Browse and navigate to the folder where to create the project.
 //    d. Click OK.
 //    e. Click Show All Files in the Solution Explorer toolbar and expand
 //       Program.cs in the Solution Explorer.
 //    f. Replace the code in Program.cs with this code.
 // 2. Add EPDM.Interop.epdm.dll as a reference (right-click the project
 //    name in the Solution Explorer, click Add Reference, click
 //    Assemblies > Framework in the left-side panel, browse to the top folder of
 //    your SOLIDWORKS PDM Professional installation, locate and select
 //    EPDM.Interop.epdm.dll, click Open, click Add, and click Close).
// 3. Change the vault name and the vault view path in the code.
// 4.   Make sure your vault contains a text file data card with a Document Number data card variable,
//    and checked-in files with data card values exactly as described in the code.
 // 5. Click Debug > Start Debugging or press F5.
 //
 // Postconditions: Press a key when prompted in the console.
 //----------------------------------------------------------------------------
  //Program.cs
 using System;
 using System.Collections.Generic;
 using System.Linq;
 using System.Text;
 using System.Threading.Tasks;
 using EPDM.Interop.epdm;

 namespace ConsoleApp1
 {
       class  Program
      {
            static  void Main(string[] args)
           {
              Console.WriteLine("Press a key...");
              Console.ReadKey();

              IEdmVault21 CurrentVault =   new EdmVault5()  as IEdmVault21;
              CurrentVault.LoginAuto("JEB5", 0);

               // The vault contains these files:             The file data cards contain these variables and values:
               // DocNum=five-six-seven Comnt=ijk.txt         @Document Number=567 & @Comment=ijk
               // DocNum=five-six-seven Comnt=xyz.txt         @Document Number=567 & @Comment=xyz
              // DocNum=one-two-three Comnt=abc.txt          @Document Number=123 & @Comment=abc

              IEdmSearchResult5 _searchResult;
              IEdmSearch9 _search = (IEdmSearch9)CurrentVault.CreateSearch2();

               // Let's see whether the IEdmSearch9 object _search works - just as an example; not needed in common practice
               string[] VarNames0 = { };
              _search.AddMultiVariableCondition(VarNames0,   "@:");   // poVariableNames can be null
              _search.GetFirstResult();
               bool OriginatedFromCreateSearch2 = _search.GetSyntaxErrors() !=  null;

              Console.WriteLine("OriginatedFromCreateSearch2 = " + OriginatedFromCreateSearch2);
              Console.WriteLine("Press a key...");
              Console.ReadKey();

               for (int i = 0; i < 7; i++)
              {
                   bool ExceptionEncountered =   false;
                  _search.Clear();
                  _search.StartFolderID = CurrentVault.GetFolderFromPath("C:\\Users\\J4M\\Desktop\\JEB5").ID;
                  switch (i)
                  {
                        case 0:      // Single variable search conditions
                                    // Expressions for special criteria and variables
                                    // Finds DocNum=five-six-seven Comnt=xyz.txt
                          Console.WriteLine("");
                          Console.WriteLine("Expressions for special criteria and variables:");
                            _search.FileName =   "(limit | cam) !wheel OR DocNum";
                            _search.AddVariable2("Document Number",  "56 & 7");
                            _search.AddVariable2("Comment",   "xy | z NOT a");

                            break;

                        case 1:      // Multi-variable condition with extended possibilities for variable names
                          Console.WriteLine("");
                          Console.WriteLine("A multi-variable condition with extended possibilities for names:");
                          {
                                string[] VarNames = {   "\"Document Number\"",    // Variable name contains a space so it must be quoted; quotes must be escaped with backslashes
                                                     "Comment",               // Extra quotes are not required for simple names
                                                     "51",                    // Database ID of Project name is a numeric constant
                                                     "_Name"                  // _Name represents file/folder name
                                                  };
                                // xy and z should be in one and the same variable value - owing to {}
                                // Text 567 can be present in a different variable of a searched document
                                // Because 567 and {z xy} can be in different variable values of the same document (and here we want to find such cases),
                                //   apply : at the beginning of the condition to turn on multi-value search logic
                                // Finds DocNum=five-six-seven Comnt=xyz.txt
                              _search.AddMultiVariableCondition(VarNames,   ":567 {z xy}");

                          }
                          break;

                        case 2:      // Multi-variable condition for all vault variables plus file/folder name
                          Console.WriteLine("");
                          Console.WriteLine("A multi-variable condition for all vault variables:");
                          {
                                string[] VarNames = {   "\"\"",    // "" represents any vault variable (and so does numeric constant 0)
                                                    "_Name"    // Unquoted _Name represents file/folder name
                                                  };
                                // Finds DocNum=five-six-seven Comnt=xyz.txt
                              _search.AddMultiVariableCondition(VarNames,   ":567 xyz | five xy");

                          }
                            break;

                        case 3:      // Multi-variable condition with mistakenly unquoted names
                          Console.WriteLine("");
                          Console.WriteLine("A multi-variable condition with mistakenly unquoted names:");
                            try
                          {
                                string[] VarNames = {   "Document Number",  "Comment",  "Project Name" };
                              // Causes an exception because there are unquoted names with spaces
                              _search.AddMultiVariableCondition(VarNames,   ":567 xyz | five xy");

                          }
                          catch (System.ArgumentException ex)
                          {
                              Console.WriteLine("Wrong variable name syntax... HRESULT = 0x" + ex.HResult.ToString("X") + ex.Message);
                              ExceptionEncountered =  true;
                          }
                            break;

                        case 4:      // Syntax errors are not displayed and no documents are returned
                          Console.WriteLine("");
                          Console.WriteLine("Non-displayed syntax errors:");
                          _search.FileName =   "(limit = | cam) !wheel OR AND DocNum";
                          _search.AddVariable2("Document Number",  "56 && 7");
                          _search.AddVariable2("Comment",   "xy | z() NOT a");

                            break;

                        case 5:      // Syntax errors are displayed (because @: is at the beginning of the conditions) and no documents are returned
                          Console.WriteLine("");
                          Console.WriteLine("Messages about syntax errors:");
                          _search.FileName =   "@:(limit = | cam) !wheel OR AND DocNum";
                          _search.AddVariable2("Document Number",  "56 && 7");
                          _search.AddVariable2("Comment",   "@:xy | z() NOT a");

                            break;

                        case 6:      // Multi-value syntax with error reporting (because @: is at the beginning of the condition)
                          Console.WriteLine("");
                          Console.WriteLine("Advanced syntax features:");
                            // The first argument, VarNames0, can be null because all the variables used are defined directly inside the second argument (condition)
                            // The second argument specifies to look for files that have (Comment = abc and any card variable containing xyz) OR (file name or "Document Number" containing 123 or ab, but not five)
                            // @: turns on multi-value logic at the top level of a condition (as does just a colon)
                            // @: allows variable bindings
                            // Finds DocNum=one-two-three Comnt=abc.txt
                          _search.AddMultiVariableCondition(VarNames0,   "@: @Comment=abc & @\"\"(xyz) | @(\"Document Number\" | _Name)(123 | ab & !five)");

                            break;
                  }

                   if (ExceptionEncountered)
                      _searchResult =   null;
                  else
                      _searchResult = _search.GetFirstResult();

                   if (_searchResult ==   null)
                      Console.WriteLine("Returned null...");
                   else
                      Console.WriteLine("Returned a file list...");
                  Console.WriteLine("Press a key...");
                  Console.ReadKey();

                   if (_searchResult !=   null)
                  {
                        while (_searchResult !=   null)
                      {
                          Console.WriteLine("NAME = " + _searchResult.Name +  ", PATH = " + _searchResult.Path);
                          Console.WriteLine("Press a key...");
                          Console.ReadKey();
                          _searchResult = _search.GetNextResult();
                      }
                  }
                   else
                  {
                        string[] SyntaxErrors = _search.GetSyntaxErrors();
                       if (SyntaxErrors !=   null)
                            foreach (string s  in SyntaxErrors)
                          {
                              Console.WriteLine(s);
                              Console.WriteLine("Press a key...");
                              Console.ReadKey();
                          }
                  }
              }
           }
      }
 }

 Back to top
```
