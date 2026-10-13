---
title: "IGetUserPreferenceTextFormat Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "IGetUserPreferenceTextFormat"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~IGetUserPreferenceTextFormat.html"
---

# IGetUserPreferenceTextFormat Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::IGetUserPreferenceTextFormat](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IGetUserPreferenceTextFormat.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetUserPreferenceTextFormat( _
   ByVal UserPreferenceValue As System.Integer _
) As TextFormat
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim UserPreferenceValue As System.Integer
Dim value As TextFormat

value = instance.IGetUserPreferenceTextFormat(UserPreferenceValue)
```

### C#

```csharp
TextFormat IGetUserPreferenceTextFormat(
   System.int UserPreferenceValue
)
```

### C++/CLI

```cpp
TextFormat^ IGetUserPreferenceTextFormat(
   System.int UserPreferenceValue
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UserPreferenceValue`:

## VBA Syntax

See [ModelDoc::IGetUserPreferenceTextFormat](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~IGetUserPreferenceTextFormat.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
