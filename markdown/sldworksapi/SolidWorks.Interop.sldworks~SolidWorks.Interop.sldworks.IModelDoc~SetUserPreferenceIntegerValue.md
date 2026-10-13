---
title: "SetUserPreferenceIntegerValue Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "SetUserPreferenceIntegerValue"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SetUserPreferenceIntegerValue.html"
---

# SetUserPreferenceIntegerValue Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::SetUserPreferenceIntegerValue](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SetUserPreferenceIntegerValue.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetUserPreferenceIntegerValue( _
   ByVal UserPreferenceValue As System.Integer, _
   ByVal Value As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim UserPreferenceValue As System.Integer
Dim Value As System.Integer
Dim value As System.Boolean

value = instance.SetUserPreferenceIntegerValue(UserPreferenceValue, Value)
```

### C#

```csharp
System.bool SetUserPreferenceIntegerValue(
   System.int UserPreferenceValue,
   System.int Value
)
```

### C++/CLI

```cpp
System.bool SetUserPreferenceIntegerValue(
   System.int UserPreferenceValue,
   System.int Value
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UserPreferenceValue`:
- `Value`:

## VBA Syntax

See [ModelDoc::SetUserPreferenceIntegerValue](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~SetUserPreferenceIntegerValue.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
