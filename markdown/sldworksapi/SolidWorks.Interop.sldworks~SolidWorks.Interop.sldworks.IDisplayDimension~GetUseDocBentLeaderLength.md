---
title: "GetUseDocBentLeaderLength Method (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "GetUseDocBentLeaderLength"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetUseDocBentLeaderLength.html"
---

# GetUseDocBentLeaderLength Method (IDisplayDimension)

Gets whether this dimension is using the document default for bent leader length or not.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetUseDocBentLeaderLength() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim value As System.Boolean

value = instance.GetUseDocBentLeaderLength()
```

### C#

```csharp
System.bool GetUseDocBentLeaderLength()
```

### C++/CLI

```cpp
System.bool GetUseDocBentLeaderLength();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if using the document default setting for dimension bent leader length, false if not

## VBA Syntax

See [DisplayDimension::GetUseDocBentLeaderLength](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~GetUseDocBentLeaderLength.html).

## Remarks

This method returns whether the document default setting is being used or not, regardless of how the dimension is currently being displayed. Even if the dimension is not currently being displayed with a bent leader, this method returns the value.

Use [IDisplayDimension::GetBentLeaderLength](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension~GetBentLeaderLength.html) to determine the bent leader length for this dimension.

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimension::SetBentLeaderLength Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetBentLeaderLength.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
