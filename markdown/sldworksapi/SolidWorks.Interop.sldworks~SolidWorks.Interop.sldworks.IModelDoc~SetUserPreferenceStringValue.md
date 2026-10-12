---
title: "SetUserPreferenceStringValue Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "SetUserPreferenceStringValue"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SetUserPreferenceStringValue.html"
---

# SetUserPreferenceStringValue Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::SetUserPreferenceStringValue](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SetUserPreferenceStringValue.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetUserPreferenceStringValue( _
   ByVal UserPreference As System.Integer, _
   ByVal Value As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim UserPreference As System.Integer
Dim Value As System.String
Dim value As System.Boolean

value = instance.SetUserPreferenceStringValue(UserPreference, Value)
```

### C#

```csharp
System.bool SetUserPreferenceStringValue(
   System.int UserPreference,
   System.string Value
)
```

### C++/CLI

```cpp
System.bool SetUserPreferenceStringValue(
   System.int UserPreference,
   System.String^ Value
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UserPreference`:
- `Value`:

## VBA Syntax

See [ModelDoc::SetUserPreferenceStringValue](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~SetUserPreferenceStringValue.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
