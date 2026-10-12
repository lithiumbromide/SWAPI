---
title: "SetFeatureManagerWidth Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "SetFeatureManagerWidth"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetFeatureManagerWidth.html"
---

# SetFeatureManagerWidth Method (IModelDoc2)

Sets the width of the FeatureManager design tree.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetFeatureManagerWidth( _
   ByVal Width As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Width As System.Integer
Dim value As System.Integer

value = instance.SetFeatureManagerWidth(Width)
```

### C#

```csharp
System.int SetFeatureManagerWidth(
   System.int Width
)
```

### C++/CLI

```cpp
System.int SetFeatureManagerWidth(
   System.int Width
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Width`: Width of the FeatureManager design tree, in pixels

### Return Value

Status of the set width operation (see **Remarks**)

## VBA Syntax

See [ModelDoc2::SetFeatureManagerWidth](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~SetFeatureManagerWidth.html).

## Examples

[Change Width of FeatureManager Design Tree (VBA)](Change_Width_of_FeatureManager_Design_Tree_Example_VB.htm)

## Remarks

The retval argument indicates the success or failure of the set width operation:

| A value of... | Indicates setting of window width... |
| --- | --- |
| 0 | Succeeded |
| -1 | Failed |

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::GetFeatureManagerWidth Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetFeatureManagerWidth.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
