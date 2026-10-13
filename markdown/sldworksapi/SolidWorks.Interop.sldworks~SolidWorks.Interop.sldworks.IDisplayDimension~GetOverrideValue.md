---
title: "GetOverrideValue Method (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "GetOverrideValue"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetOverrideValue.html"
---

# GetOverrideValue Method (IDisplayDimension)

Gets the value to display instead of the actual dimension value.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetOverrideValue() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim value As System.Double

value = instance.GetOverrideValue()
```

### C#

```csharp
System.double GetOverrideValue()
```

### C++/CLI

```cpp
System.double GetOverrideValue();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Value to display instead of the actual dimension value

## VBA Syntax

See [DisplayDimension::GetOverrideValue](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~GetOverrideValue.html).

## Remarks

Use [IDisplayDimension::GetOverride](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension~GetOverride.html) to get whether to display the actual dimension value or to override it with another value.

Use [IDisplayDimension::SetOverride](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension~SetOverride.html) to set whether to override the actual dimension value with another value, and, if so, that value.

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
