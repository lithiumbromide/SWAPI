---
title: "InsertFeatureShellAddThickness Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "InsertFeatureShellAddThickness"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertFeatureShellAddThickness.html"
---

# InsertFeatureShellAddThickness Method (IModelDoc2)

Adds thickness to a face in a multi-thickness shell feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertFeatureShellAddThickness( _
   ByVal Thickness As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Thickness As System.Double

instance.InsertFeatureShellAddThickness(Thickness)
```

### C#

```csharp
void InsertFeatureShellAddThickness(
   System.double Thickness
)
```

### C++/CLI

```cpp
void InsertFeatureShellAddThickness(
   System.double Thickness
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Thickness`: Shell thickness in meters

## VBA Syntax

See [ModelDoc2::InsertFeatureShellAddThickness](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~InsertFeatureShellAddThickness.html).

## Remarks

This method works with [IModelDoc2::InsertFeatureShell](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~InsertFeatureShell.html) to create a multi-thickness shell as follows:

1. Select the faces to remove to create the shell feature by calling [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html) with Marks of 1.
2. Select faces with alternate thicknesses using Marks of 2.
3. Call this method once for each of the faces selected in step 2.
4. Call IModelDoc2::InsertFeatureShell.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
