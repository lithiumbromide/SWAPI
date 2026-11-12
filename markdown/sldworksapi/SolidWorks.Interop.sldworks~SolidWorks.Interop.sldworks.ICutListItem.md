---
title: "ICutListItem Interface"
project: "SOLIDWORKS API Help"
interface: "ICutListItem"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICutListItem.html"
---

# ICutListItem Interface

Allows access to a configuration-specific cut list folder.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ICutListItem
```

### Visual Basic (Usage)

```vb
Dim instance As ICutListItem
```

### C#

```csharp
public interface ICutListItem
```

### C++/CLI

```cpp
public interface class ICutListItem
```

## VBA Syntax

See [CutListItem](ms-its:sldworksapivb6.chm::/sldworks~CutListItem.html).

## Examples

'VBA

'Preconditions:

' 1. Open a part that has one or more configuration-specific cut lists with custom properties. (Or you can ask SOLIDWORKS API Support to send the models that work with this ICutListItem sample code.)

' 2. Open an Immediate window.

'Postconditions: Inspect all the configurations' cut lists' custom properties in the Immediate window.

'=============================================================

Option Explicit
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim vConfigNameArr As Variant
Dim vConfigName As Variant
Dim vcutlistItems As Variant
Dim vcutlistItem As Variant
Dim cutlistItem As SldWorks.CutListItem
Dim cusPropMgr As SldWorks.CustomPropertyManager
Dim config As SldWorks.Configuration
Dim lRetVal As Long
Dim vPropNames As Variant
Dim vPropTypes As Variant
Dim vPropValues As Variant
Dim resolved() As Long
Dim linkProp() As Long
Dim i As Long
Dim j As Long
Dim propName As Variant

Sub main()

Set swApp = Application.SldWorks
Set swModel = swApp.**ActiveDoc**

vConfigNameArr = swModel.**GetConfigurationNames**()
For Each vConfigName In vConfigNameArr
Debug.Print "Configuration: " & vConfigName
Set config = swModel.**GetConfigurationByName**(vConfigName)
vcutlistItems = config.**GetCutListItems**()
i = 1
For Each vcutlistItem In vcutlistItems
Debug.Print "Cut list item #" & i & " custom properties:"
Set cutlistItem = vcutlistItem
Set cusPropMgr = cutlistItem.**CustomPropertyManager**()
lRetVal = cusPropMgr.**GetAll3**(vPropNames, vPropTypes, vPropValues, resolved, linkProp)
j = 0
For Each propName In vPropNames
Debug.Print " " & propName & " " & vPropValues(j)
j = j + 1
Next
i = i + 1
Next
Next

End Sub

## Examples

[Get Configuration-specific Cut List Custom Properties (VB.NET)](Get_Configuration-specific_Cut_List_Custom_Properties_Example_VBNET.htm)
[Get Configuration-specific Cut List Custom Properties (C#)](Get_Configuration-specific_Cut_List_Custom_Properties_Example_CSharp.htm)

## Accessors

[IConfiguration::GetCutListItems](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetCutListItems.html)

## Access Diagram

[CutListItem](SWObjectModel.pdf#CutListItem)

## See Also

[ICutListItem Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICutListItem_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
