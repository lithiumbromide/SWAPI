---
title: "SetValueVariables Method (IEdmEnumeratorVariable9)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmEnumeratorVariable9"
member: "SetValueVariables"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable9~SetValueVariables.html"
---

# SetValueVariables Method (IEdmEnumeratorVariable9)

Sets the values of file variables.

## Syntax

### Visual Basic

```vb
Sub SetValueVariables( _
   ByVal poVarNamesList As EdmStrLst5, _
   ByVal poVarValuesList As EdmStrLst5, _
   ByVal bsCfgName As System.String, _
   Optional ByVal bOnlyIfPartOfCard As System.Boolean _
)
```

### C#

```csharp
void SetValueVariables(
   EdmStrLst5 poVarNamesList,
   EdmStrLst5 poVarValuesList,
   System.string bsCfgName,
   System.bool bOnlyIfPartOfCard
)
```

### C++/CLI

```cpp
void SetValueVariables(
   EdmStrLst5^ poVarNamesList,
   EdmStrLst5^ poVarValuesList,
   System.String^ bsCfgName,
   System.bool bOnlyIfPartOfCard
)
```

### Parameters

- `poVarNamesList`: [IEdmStrLst5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmStrLst5.html)

; list of variable names
- `poVarValuesList`: [IEdmStrLst5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmStrLst5.html)

; list of values for variable names in poVarNamesList
- `bsCfgName`: Configuration name
- `bOnlyIfPartOfCard`: True to set the variable only if the variable is part of the data card, false to always set the variable (see

Remarks

)

## Remarks

This method can write the value to the file if the variable is mapped to a custom property.

## See Also

[IEdmEnumeratorVariable9 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable9.html)

[IEdmEnumeratorVariable9 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable9_members.html)

## Availability

SOLIDWORKS PDM Professional 2012
