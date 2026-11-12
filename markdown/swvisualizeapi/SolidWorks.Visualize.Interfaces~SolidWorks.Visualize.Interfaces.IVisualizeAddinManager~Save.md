---
title: "Save Method (IVisualizeAddinManager)"
project: "SOLIDWORKS Visualize Add-in API Help"
interface: "IVisualizeAddinManager"
member: "Save"
kind: "method"
source: "swvisualizeapi/SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IVisualizeAddinManager~Save.html"
---

# Save Method (IVisualizeAddinManager)

Obsolete. Superseded by [IVisualizeAddinManager2::SaveWithPartGrouping](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IVisualizeAddinManager2~SaveWithPartGrouping.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub Save( _
   ByVal filename As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IVisualizeAddinManager
Dim filename As System.String

instance.Save(filename)
```

### C#

```csharp
void Save(
   System.string filename
)
```

### C++/CLI

```cpp
void Save(
   System.String^ filename
)
```

### Parameters

- `filename`: Visualize Project file name (***.SVPJ**)

## VBA Syntax

See [IVisualizeAddinManager::Save](ms-its:swvisualizeapivb6.chm::/SolidWorks_Visualize_Interfaces~IVisualizeAddinManager~Save.html).

## See Also

[IVisualizeAddinManager Interface](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IVisualizeAddinManager.html)
[IVisualizeAddinManager Members](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IVisualizeAddinManager_members.html)

## Availability

SOLIDWORKS Visualize Add-in API 2025 FCS
