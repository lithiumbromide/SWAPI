---
title: "ConvertToUserUnit Method (IUserUnit)"
project: "SOLIDWORKS API Help"
interface: "IUserUnit"
member: "ConvertToUserUnit"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit~ConvertToUserUnit.html"
---

# ConvertToUserUnit Method (IUserUnit)

Converts the input value to document units.

## Syntax

### Visual Basic (Declaration)

```vb
Function ConvertToUserUnit( _
   ByVal ValueIn As System.Double, _
   ByVal ShowUsernames As System.Boolean, _
   ByVal NameInEnglish As System.Boolean _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IUserUnit
Dim ValueIn As System.Double
Dim ShowUsernames As System.Boolean
Dim NameInEnglish As System.Boolean
Dim value As System.String

value = instance.ConvertToUserUnit(ValueIn, ShowUsernames, NameInEnglish)
```

### C#

```csharp
System.string ConvertToUserUnit(
   System.double ValueIn,
   System.bool ShowUsernames,
   System.bool NameInEnglish
)
```

### C++/CLI

```cpp
System.String^ ConvertToUserUnit(
   System.double ValueIn,
   System.bool ShowUsernames,
   System.bool NameInEnglish
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ValueIn`: Value to convert
- `ShowUsernames`: True to show the user names, false to not
- `NameInEnglish`: True to return the name in English, false to not

### Return Value

Conversion to a string

## VBA Syntax

See [UserUnit::ConvertToUserUnit](ms-its:sldworksapivb6.chm::/sldworks~UserUnit~ConvertToUserUnit.html).

## Examples

See the [IUserUnit](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit.html) examples.

## See Also

[IUserUnit Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit.html)
[IUserUnit Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit_members.html)
[IUserUnit::ConvertDoubleToSystemValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit~ConvertDoubleToSystemValue.html)
[IUserUnit::ConvertToSystemValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit~ConvertToSystemValue.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
