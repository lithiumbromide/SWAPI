---
title: "ConvertDoubleToSystemValue Method (IUserUnit)"
project: "SOLIDWORKS API Help"
interface: "IUserUnit"
member: "ConvertDoubleToSystemValue"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit~ConvertDoubleToSystemValue.html"
---

# ConvertDoubleToSystemValue Method (IUserUnit)

Converts a double value to a document unit value.

## Syntax

### Visual Basic (Declaration)

```vb
Function ConvertDoubleToSystemValue( _
   ByVal UserValue As System.Double _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IUserUnit
Dim UserValue As System.Double
Dim value As System.Double

value = instance.ConvertDoubleToSystemValue(UserValue)
```

### C#

```csharp
System.double ConvertDoubleToSystemValue(
   System.double UserValue
)
```

### C++/CLI

```cpp
System.double ConvertDoubleToSystemValue(
   System.double UserValue
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UserValue`: Value to convert

### Return Value

Converted document unit value

## VBA Syntax

See [UserUnit::ConvertDoubleToSystemValue](ms-its:sldworksapivb6.chm::/sldworks~UserUnit~ConvertDoubleToSystemValue.html).

## Examples

See the [IUserUnit](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit.html) examples.

## See Also

[IUserUnit Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit.html)
[IUserUnit Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit_members.html)
[IUserUnit::ConvertToSystemValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit~ConvertToSystemValue.html)
[IUserUnit::ConvertToUserUnit Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit~ConvertToUserUnit.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
