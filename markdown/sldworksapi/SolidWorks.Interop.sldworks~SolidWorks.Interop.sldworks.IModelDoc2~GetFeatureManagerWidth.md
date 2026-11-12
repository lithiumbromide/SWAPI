---
title: "GetFeatureManagerWidth Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "GetFeatureManagerWidth"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetFeatureManagerWidth.html"
---

# GetFeatureManagerWidth Method (IModelDoc2)

Gets the width of the FeatureManager design tree.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFeatureManagerWidth() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As System.Integer

value = instance.GetFeatureManagerWidth()
```

### C#

```csharp
System.int GetFeatureManagerWidth()
```

### C++/CLI

```cpp
System.int GetFeatureManagerWidth();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Width

## VBA Syntax

See [ModelDoc2::GetFeatureManagerWidth](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~GetFeatureManagerWidth.html).

## Examples

[Change Width of FeatureManager Design Tree (VBA)](Change_Width_of_FeatureManager_Design_Tree_Example_VB.htm)

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[SetFeatureManagerWidth Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetFeatureManagerWidth.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
