---
title: "Get COLORREF Values of Standard User-interface Elements (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_COLORREF_Values_of_Standard_User-interface_Elements_Example_CSharp.htm"
---

# Get COLORREF Values of Standard User-interface Elements (C#)

This example shows how to get the COLORREF values of standard SOLIDWORKS Design user-interface elements.

//---------------------------------------------------------
// Preconditions: Open the Immediate window.
//
// Postconditions:
// 1. Prints the names of the SOLIDWORKS Design standard
// user-interface, elements (dimensions, backgrounds,
// drawing paper, sketch status, annotations, etc.) and
// their COLORREF values to the Immediate window.
// 2. Examine the Immediate window.
//--------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;

namespace ColorTableCSharp.csproj
{

partial class SolidWorksMacro
{

public void Main()
{
ColorTable swColorTable = default(ColorTable);
int standardCount = 0;
int count = 0;
string colorName = null;
int colorRef = 0;

swColorTable = (ColorTable)swApp.**GetColorTable**();

standardCount = swColorTable.**GetStandardCount**();
Debug.Print("SOLIDWORKS Design standard user-interface element and COLORREF value:");
// Iterate through standard colors
for (count = 0; count <= (standardCount - 1); count++)
{
// Get the entry name
colorName = swColorTable.**GetNameAtIndex**(count);
if (!string.IsNullOrEmpty(colorName))
{
// Get the entry's COLORREF
colorRef = swColorTable.**GetColorRefAtIndex**(count);
Debug.Print(" " + colorName + " : " + colorRef);
}
else
{
}
}

}

/// <summary>
/// The SldWorks swApp variable is pre-assigned for you.
/// </summary>

public SldWorks swApp;
}
}
