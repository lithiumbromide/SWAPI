---
title: "SetUserPreferenceDoubleValue Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "SetUserPreferenceDoubleValue"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SetUserPreferenceDoubleValue.html"
---

# SetUserPreferenceDoubleValue Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::SetUserPreferenceDoubleValue](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SetUserPreferenceDoubleValue.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetUserPreferenceDoubleValue( _
   ByVal UserPreferenceValue As System.Integer, _
   ByVal Value As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim UserPreferenceValue As System.Integer
Dim Value As System.Double
Dim value As System.Boolean

value = instance.SetUserPreferenceDoubleValue(UserPreferenceValue, Value)
```

### C#

```csharp
System.bool SetUserPreferenceDoubleValue(
   System.int UserPreferenceValue,
   System.double Value
)
```

### C++/CLI

```cpp
System.bool SetUserPreferenceDoubleValue(
   System.int UserPreferenceValue,
   System.double Value
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UserPreferenceValue`:
- `Value`:

## VBA Syntax

See [ModelDoc::SetUserPreferenceDoubleValue](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~SetUserPreferenceDoubleValue.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
