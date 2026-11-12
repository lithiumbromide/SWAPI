---
title: "GetBentLeaderLength Method (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "GetBentLeaderLength"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetBentLeaderLength.html"
---

# GetBentLeaderLength Method (IDisplayDimension)

Gets the length of the bent leader to use when displaying this dimension.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBentLeaderLength() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim value As System.Double

value = instance.GetBentLeaderLength()
```

### C#

```csharp
System.double GetBentLeaderLength()
```

### C++/CLI

```cpp
System.double GetBentLeaderLength();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Length of the bent leader in system units

## VBA Syntax

See [DisplayDimension::GetBentLeaderLength](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~GetBentLeaderLength.html).

## Remarks

This method returns the length of the bent leader regardless of how the dimension is currently being displayed. Even if the dimension is not currently being displayed with a bent leader, this method still returns the length.

If the dimension is using the document default setting for dimension bent leader length, this method returns that value. You can use [IDisplayDimension::GetUseDocBentLeaderLength](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension~GetUseDocBentLeaderLength.html) to determine if this dimension is using the document default setting for dimension
bent leader length or not.

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimension::SetBentLeaderLength Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetBentLeaderLength.html)
[IDisplayDimension::GetUseDocBentLeaderLength Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetUseDocBentLeaderLength.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
