---
title: "InsertAlternateView Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "InsertAlternateView"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertAlternateView.html"
---

# InsertAlternateView Method (IView)

Inserts an **Alternate Position View** of the currently selected drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertAlternateView( _
   ByVal ConfigurationName As System.String _
) As View
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim ConfigurationName As System.String
Dim value As View

value = instance.InsertAlternateView(ConfigurationName)
```

### C#

```csharp
View InsertAlternateView(
   System.string ConfigurationName
)
```

### C++/CLI

```cpp
View^ InsertAlternateView(
   System.String^ ConfigurationName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ConfigurationName`: Name of the configuration (see Remarks)

### Return Value

Alternate [drawing view](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView.html)

## VBA Syntax

See [View::InsertAlternateView](ms-its:sldworksapivb6.chm::/sldworks~View~InsertAlternateView.html).

## Examples

[Insert Alternate Position View (VBA)](Insert_Alternate_Position_View_Example_VB.htm)

## Remarks

Before using this method, you must select a drawing view on which to superimpose the Alternate Position View.

If you specify a non-existent configuration for ConfigurationName, then it is created using all default settings. The new configuration is identical to the currently selected configuration. The user can then open the assembly, edit the configuration, and update the drawing view

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
