---
title: "InsertFeatureShell Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "InsertFeatureShell"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertFeatureShell.html"
---

# InsertFeatureShell Method (IModelDoc2)

Creates a shell feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertFeatureShell( _
   ByVal Thickness As System.Double, _
   ByVal Outward As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Thickness As System.Double
Dim Outward As System.Boolean

instance.InsertFeatureShell(Thickness, Outward)
```

### C#

```csharp
void InsertFeatureShell(
   System.double Thickness,
   System.bool Outward
)
```

### C++/CLI

```cpp
void InsertFeatureShell(
   System.double Thickness,
   System.bool Outward
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Thickness`: Shell thickness in meters
- `Outward`: True for outside, false for inside

## VBA Syntax

See [ModelDoc2::InsertFeatureShell](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~InsertFeatureShell.html).

## Examples

[Create Shell Feature (VBA)](Get_Shell_Feature_Data_Example_VB.htm)
[Create Shell Feature (VB.NET)](Create_Shell_Feature_Example_VBNET.htm)
[Create Shell Feature (C#)](Create_Shell_Feature_Example_CSharp.htm)

## Remarks

Before calling this method, select faces to remove to create the shell using [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html) with Marks of 1. See the SOLIDWORKS Help for information about what entities are valid for selection.

To make a multi-thickness shell, use this method with [IModelDoc2::InsertFeatureShellAddThickness](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~InsertFeatureShellAddThickness.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IShellFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
