---
title: "GetUniqueName Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetUniqueName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetUniqueName.html"
---

# GetUniqueName Method (IView)

Gets the unique name of this section view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetUniqueName() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.String

value = instance.GetUniqueName()
```

### C#

```csharp
System.string GetUniqueName()
```

### C++/CLI

```cpp
System.String^ GetUniqueName();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Name of this section view

## VBA Syntax

See [View::GetUniqueName](ms-its:sldworksapivb6.chm::/sldworks~View~GetUniqueName.html).

## Examples

[Get Unique Name of Section View (VBA)](Get_Unique_Name_of_Section_View_Example_VB.htm)
[Get Unique Name of Section View (VB.NET)](Get_Unique_Name_of_Section_View_Example_VBNET.htm)
[Get Unique Name of Section View (C#)](Get_Unique_Name_of_Section_View_Example_CSharp.htm)

## Remarks

Before selecting a specific section view using [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html), call this method to get the unique name of the section view in "Drawing View`number`" format.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetName2.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
