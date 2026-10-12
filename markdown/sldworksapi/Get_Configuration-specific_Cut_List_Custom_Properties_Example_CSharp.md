---
title: "Get Configuration-specific Cut List Custom Properties Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Configuration-specific_Cut_List_Custom_Properties_Example_CSharp.htm"
---

# Get Configuration-specific Cut List Custom Properties Example (C#)

This example shows how to get configuration-specific cut list custom properties.

// ===========================================================

// Preconditions:

// 1. Open a part that has one or more configuration-specific cut lists with custom properties.

// (Or ask SOLIDWORKS API Support to send you the models that work with this ICutListItem sample code.)

// 2. Open an Immediate/Output window.

//

// Postconditions: Inspect all the configurations' cut lists' custom properties in the Immediate/Output window.

// =============================================================

using System;

using System.Collections.Generic;

using System.Linq;

using System.Text;

using System.Threading.Tasks;

using System.Windows;

using System.Windows.Forms;

using SolidWorks.Interop.sldworks;

using SolidWorks.Interop.swconst;

using System.Diagnostics;

namespace ConfigSpecCutListCustomProps_CSharp

{

public partial class SolidWorksMacro

{

ModelDoc2 swModel;

string[] vConfigNameArr;

string vConfigName;

object[] cutlistobj;

CutListItem[] vcutlistItems;

CutListItem vcutlistItem;

CutListItem cutlistItem;

CustomPropertyManager cusPropMgr;

Configuration config;

int lRetVal;

object vPropNames;

object vPropTypes;

object vPropValues;

object resolved;

object linkProp;

int i;

int j;

string propName;

public void Main()

{

swModel = (ModelDoc2)swApp.**ActiveDoc**;

vConfigNameArr = (string[])swModel.**GetConfigurationNames**();

foreach (var vConfigName in vConfigNameArr)

{

Debug.Print("Configuration: " + vConfigName);

config = (Configuration)swModel.**GetConfigurationByName**(vConfigName);

cutlistobj = (object[])config.**GetCutListItems**();

int n;

for (n=0; n < cutlistobj.Length; n++)

{

vcutlistItem = (CutListItem)cutlistobj[n];

Debug.Print("Cut list item #" + n + " custom properties:");

cusPropMgr = vcutlistItem.**CustomPropertyManager**;

lRetVal = cusPropMgr.**GetAll3**(ref vPropNames, ref vPropTypes, ref vPropValues, ref resolved, ref linkProp);

object[] propValues = (object[])vPropValues;

string[] propNames = (string[])vPropNames;

for (j = 0; j < lRetVal; j++)

{

Debug.Print(" " + propNames[j] + " " + propValues[j]);

}

i = i + 1;

}

}

}

// The SldWorks swApp variable is pre-assigned for you.

public SldWorks swApp;

}

}
