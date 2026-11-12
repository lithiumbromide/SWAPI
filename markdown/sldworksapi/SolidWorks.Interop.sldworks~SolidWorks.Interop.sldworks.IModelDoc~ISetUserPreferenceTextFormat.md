---
title: "ISetUserPreferenceTextFormat Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "ISetUserPreferenceTextFormat"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~ISetUserPreferenceTextFormat.html"
---

# ISetUserPreferenceTextFormat Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::ISetUserPreferenceTextFormat](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ISetUserPreferenceTextFormat.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ISetUserPreferenceTextFormat( _
   ByVal UserPreferenceValue As System.Integer, _
   ByVal Value As TextFormat _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim UserPreferenceValue As System.Integer
Dim Value As TextFormat
Dim value As System.Boolean

value = instance.ISetUserPreferenceTextFormat(UserPreferenceValue, Value)
```

### C#

```csharp
System.bool ISetUserPreferenceTextFormat(
   System.int UserPreferenceValue,
   TextFormat Value
)
```

### C++/CLI

```cpp
System.bool ISetUserPreferenceTextFormat(
   System.int UserPreferenceValue,
   TextFormat^ Value
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UserPreferenceValue`:
- `Value`:

## VBA Syntax

See [ModelDoc::ISetUserPreferenceTextFormat](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~ISetUserPreferenceTextFormat.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
