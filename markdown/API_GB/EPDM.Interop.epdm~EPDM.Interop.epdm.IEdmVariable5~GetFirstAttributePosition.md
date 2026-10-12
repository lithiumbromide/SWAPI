---
title: "GetFirstAttributePosition Method (IEdmVariable5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVariable5"
member: "GetFirstAttributePosition"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVariable5~GetFirstAttributePosition.html"
---

# GetFirstAttributePosition Method (IEdmVariable5)

Starts an enumeration of the attributes to which this variable is mapped for the specified file type.

## Syntax

### Visual Basic

```vb
Function GetFirstAttributePosition( _
   ByVal bsFileExtension As System.String _
) As IEdmPos5
```

### C#

```csharp
IEdmPos5 GetFirstAttributePosition(
   System.string bsFileExtension
)
```

### C++/CLI

```cpp
IEdmPos5^ GetFirstAttributePosition(
   System.String^ bsFileExtension
)
```

### Parameters

- `bsFileExtension`: Extension of file for which to get attributes, e.g., "DWG" or "DOC"; "" to get all attributes for all file types

### Return Value

[IEdmPos5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html); position of the first attribute in the enumeration

## Examples

[Find Data Cards with Description Variable (C#)](Find_Data_Cards_with_Description_Variable_Example_CSharp.htm)
[Find Data Cards with Description Variable (VB.NET)](Find_Data_Cards_with_Description_Variable_Example_VBNET.htm)

## Remarks

A variable in SOLIDWORKS PDM Professional can be mapped to zero or more block-attribute pairs. SOLIDWORKS PDM Professional uses the attributes when transferring data between the file data card and the file, itself. See the main SOLIDWORKS PDM Professional online help for more information.

After calling this method, pass the returned position of the first attribute to [IEdmVariable5::GetNextAttribute](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVariable5~GetNextAttribute.html) to get the first attribute in this list. Then call IEdmVariable5::GetNextAttribute repeatedly to get the rest of the attributes.

C++ users not using smart-pointer wrapper functions must release the returned interface, IEdmPos5.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmVariable5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVariable5.html)
[IEdmVariable5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVariable5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
