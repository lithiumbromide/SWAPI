---
title: "Status Method (IShutOffSurfaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IShutOffSurfaceFeatureData"
member: "Status"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~Status.html"
---

# Status Method (IShutOffSurfaceFeatureData)

Gets the status of the shut-off surface feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function Status() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IShutOffSurfaceFeatureData
Dim value As System.Integer

value = instance.Status()
```

### C#

```csharp
System.int Status()
```

### C++/CLI

```cpp
System.int Status();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Status as defined in [swShutOffSurfaceFeatureStatus_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swShutOffSurfaceFeatureStatus_e.html)

## VBA Syntax

See [ShutOffSurfaceFeatureData::Status](ms-its:sldworksapivb6.chm::/sldworks~ShutOffSurfaceFeatureData~Status.html).

## Examples

See [IShutOffSurfaceFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IShutOffSurfaceFeatureData.html) examples.

## See Also

[IShutOffSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData.html)
[IShutOffSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
