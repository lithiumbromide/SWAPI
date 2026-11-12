---
title: "GetArcLengthLeader Method (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "GetArcLengthLeader"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetArcLengthLeader.html"
---

# GetArcLengthLeader Method (IDisplayDimension)

Gets the leader style of this arc length dimension.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetArcLengthLeader() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim value As System.Integer

value = instance.GetArcLengthLeader()
```

### C#

```csharp
System.int GetArcLengthLeader()
```

### C++/CLI

```cpp
System.int GetArcLengthLeader();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Annotation

## VBA Syntax

See [DisplayDimension::GetArcLengthLeader](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~GetArcLengthLeader.html).

## Remarks

The [IAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation.html) object is a higher-level object that contains methods that are general to all types of annotations.

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimension::SetArcLengthLeader Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetArcLengthLeader.html)

## Availability

SOLIDWORKS 99, datecode 1999207
