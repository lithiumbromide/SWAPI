---
title: "GetModelViewNames Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "GetModelViewNames"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetModelViewNames.html"
---

# GetModelViewNames Method (IModelDoc2)

Gets a list containing the names of each model view in this document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetModelViewNames() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As System.Object

value = instance.GetModelViewNames()
```

### C#

```csharp
System.object GetModelViewNames()
```

### C++/CLI

```cpp
System.Object^ GetModelViewNames();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array containing the names of each model view in this document

## VBA Syntax

See [ModelDoc2::GetModelViewNames](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~GetModelViewNames.html).

## Examples

[Get View Mode Names for Model (VBA)](Get_View_Mode_Names_for_Model_Example_VB.htm)

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::ModelViewManager Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ModelViewManager.html)
[IModelDoc2::IActiveView Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IActiveView.html)
[IModelDoc2::ActiveView Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ActiveView.html)
[IModelDoc2::IGetModelViewNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetModelViewNames.html)
[IModelDoc2::GetModelViewCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetModelViewCount.html)
[IModelDoc2::IGetFirstModelView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetFirstModelView.html)
[IModelDoc2::GetFirstModelView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetFirstModelView.html)
[IModelDoc2::EnumModelViews Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EnumModelViews.html)
[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
