---
title: "ConvertToSystemValue Method (IUserUnit)"
project: "SOLIDWORKS API Help"
interface: "IUserUnit"
member: "ConvertToSystemValue"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit~ConvertToSystemValue.html"
---

# ConvertToSystemValue Method (IUserUnit)

Converts a text string to a document unit value.

## Syntax

### Visual Basic (Declaration)

```vb
Function ConvertToSystemValue( _
   ByVal UnitText As System.String, _
   ByRef ComputedValue As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IUserUnit
Dim UnitText As System.String
Dim ComputedValue As System.Double
Dim value As System.Boolean

value = instance.ConvertToSystemValue(UnitText, ComputedValue)
```

### C#

```csharp
System.bool ConvertToSystemValue(
   System.string UnitText,
   out System.double ComputedValue
)
```

### C++/CLI

```cpp
System.bool ConvertToSystemValue(
   System.String^ UnitText,
   [Out] System.double ComputedValue
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UnitText`: Value to convert
- `ComputedValue`: Converted value in document units

### Return Value

True if successful, false if not

## VBA Syntax

See [UserUnit::ConvertToSystemValue](ms-its:sldworksapivb6.chm::/sldworks~UserUnit~ConvertToSystemValue.html).

## Examples

See the [IUserUnit](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit.html) examples.

## Remarks

This takes the value directly from a textbox control and passes it in to convert to a double value.

This imitates the behavior of when working in the SOLIDWORKS Design user interface and passing a value like "10 / 2" into one of the values on a dialog box.

## See Also

[IUserUnit Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit.html)
[IUserUnit Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit_members.html)
[IUserUnit::ConvertDoubleToSystemValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit~ConvertDoubleToSystemValue.html)
[IUserUnit::ConvertToUserUnit Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit~ConvertToUserUnit.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
