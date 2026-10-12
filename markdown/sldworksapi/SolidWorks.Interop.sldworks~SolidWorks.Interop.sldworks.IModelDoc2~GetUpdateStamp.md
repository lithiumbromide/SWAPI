---
title: "GetUpdateStamp Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "GetUpdateStamp"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetUpdateStamp.html"
---

# GetUpdateStamp Method (IModelDoc2)

Gets the current update stamp for this document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetUpdateStamp() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As System.Integer

value = instance.GetUpdateStamp()
```

### C#

```csharp
System.int GetUpdateStamp()
```

### C++/CLI

```cpp
System.int GetUpdateStamp();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Current update stamp value for this document

## VBA Syntax

See [ModelDoc2::GetUpdateStamp](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~GetUpdateStamp.html).

## Remarks

The update stamp is an integer form of a time stamp. The update stamp is incremented for model state changes (i.e., suppress or unsuppress, configuration changes, feature changes, etc.) and for geometric changes (i.e., anything that requires a rebuild). This time stamp is not incremented for operations such as color changes, feature or configuration name changes, etc.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IFeature::GetUpdateStamp Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetUpdateStamp.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
