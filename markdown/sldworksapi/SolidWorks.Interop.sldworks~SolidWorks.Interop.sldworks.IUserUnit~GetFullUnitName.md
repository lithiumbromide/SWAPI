---
title: "GetFullUnitName Method (IUserUnit)"
project: "SOLIDWORKS API Help"
interface: "IUserUnit"
member: "GetFullUnitName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit~GetFullUnitName.html"
---

# GetFullUnitName Method (IUserUnit)

Gets the full name of the unit.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFullUnitName( _
   ByVal Plural As System.Boolean _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IUserUnit
Dim Plural As System.Boolean
Dim value As System.String

value = instance.GetFullUnitName(Plural)
```

### C#

```csharp
System.string GetFullUnitName(
   System.bool Plural
)
```

### C++/CLI

```cpp
System.String^ GetFullUnitName(
   System.bool Plural
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Plural`: True if the name of the unit is plural, false if not

### Return Value

Full name of the unit

## VBA Syntax

See [UserUnit::GetFullUnitName](ms-its:sldworksapivb6.chm::/sldworks~UserUnit~GetFullUnitName.html).

## Examples

See the [IUserUnit](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit.html) examples.

## See Also

[IUserUnit Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit.html)
[IUserUnit Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit_members.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
