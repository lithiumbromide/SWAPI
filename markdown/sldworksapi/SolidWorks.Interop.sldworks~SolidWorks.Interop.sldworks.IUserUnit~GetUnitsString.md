---
title: "GetUnitsString Method (IUserUnit)"
project: "SOLIDWORKS API Help"
interface: "IUserUnit"
member: "GetUnitsString"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit~GetUnitsString.html"
---

# GetUnitsString Method (IUserUnit)

Gets the string that describes the unit.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetUnitsString( _
   ByVal InEnglish As System.Boolean _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IUserUnit
Dim InEnglish As System.Boolean
Dim value As System.String

value = instance.GetUnitsString(InEnglish)
```

### C#

```csharp
System.string GetUnitsString(
   System.bool InEnglish
)
```

### C++/CLI

```cpp
System.String^ GetUnitsString(
   System.bool InEnglish
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `InEnglish`: True to return the string in English, false to not

### Return Value

String describing the unit

## VBA Syntax

See [UserUnit::GetUnitsString](ms-its:sldworksapivb6.chm::/sldworks~UserUnit~GetUnitsString.html).

## Examples

See the [IUserUnit](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit.html) examples.

## See Also

[IUserUnit Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit.html)
[IUserUnit Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit_members.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
