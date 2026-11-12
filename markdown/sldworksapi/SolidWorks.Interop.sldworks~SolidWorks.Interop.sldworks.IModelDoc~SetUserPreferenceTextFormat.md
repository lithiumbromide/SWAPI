---
title: "SetUserPreferenceTextFormat Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "SetUserPreferenceTextFormat"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SetUserPreferenceTextFormat.html"
---

# SetUserPreferenceTextFormat Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::SetUserPreferenceTextFormat](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SetUserPreferenceTextFormat.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetUserPreferenceTextFormat( _
   ByVal UserPreferenceValue As System.Integer, _
   ByVal Value As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim UserPreferenceValue As System.Integer
Dim Value As System.Object
Dim value As System.Boolean

value = instance.SetUserPreferenceTextFormat(UserPreferenceValue, Value)
```

### C#

```csharp
System.bool SetUserPreferenceTextFormat(
   System.int UserPreferenceValue,
   System.object Value
)
```

### C++/CLI

```cpp
System.bool SetUserPreferenceTextFormat(
   System.int UserPreferenceValue,
   System.Object^ Value
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UserPreferenceValue`:
- `Value`:

## VBA Syntax

See [ModelDoc::SetUserPreferenceTextFormat](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~SetUserPreferenceTextFormat.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
