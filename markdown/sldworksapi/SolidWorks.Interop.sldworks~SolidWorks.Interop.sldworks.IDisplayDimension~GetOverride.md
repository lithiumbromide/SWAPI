---
title: "GetOverride Method (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "GetOverride"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetOverride.html"
---

# GetOverride Method (IDisplayDimension)

Gets whether to display the actual dimension value or to override it with another value.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetOverride() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim value As System.Boolean

value = instance.GetOverride()
```

### C#

```csharp
System.bool GetOverride()
```

### C++/CLI

```cpp
System.bool GetOverride();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True to display the override value, false to display the actual dimension value

## VBA Syntax

See [DisplayDimension::GetOverride](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~GetOverride.html).

## Remarks

Use [IDisplayDimension::GetOverrideValue](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension~GetOverrideValue.html) to get the override value.

Use [IDisplayDimension::SetOverride](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension~SetOverride.html) to set whether to override the actual dimension value with another value and, if so, that value.

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
