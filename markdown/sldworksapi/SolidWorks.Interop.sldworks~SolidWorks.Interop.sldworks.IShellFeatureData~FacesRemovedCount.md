---
title: "FacesRemovedCount Property (IShellFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IShellFeatureData"
member: "FacesRemovedCount"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~FacesRemovedCount.html"
---

# FacesRemovedCount Property (IShellFeatureData)

Gets the number of faces removed in this shell feature.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property FacesRemovedCount As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IShellFeatureData
Dim value As System.Integer

value = instance.FacesRemovedCount
```

### C#

```csharp
System.int FacesRemovedCount {get;}
```

### C++/CLI

```cpp
property System.int FacesRemovedCount {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Number of removed faces

## VBA Syntax

See [ShellFeatureData::FacesRemovedCount](ms-its:sldworksapivb6.chm::/sldworks~ShellFeatureData~FacesRemovedCount.html).

## Examples

See the [IShellFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData.html) examples.

## Remarks

Call this property before calling [IShellFeatureData::IGetFacesRemoved](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IShellFeatureData~IGetFacesRemoved.html) to get the size of the array for that method.

## See Also

[IShellFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData.html)
[IShellFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData_members.html)
[IShellFeatureData::ISetFacesRemoved Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~ISetFacesRemoved.html)
[IShellFeatureData::FacesRemoved Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~FacesRemoved.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
