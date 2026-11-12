---
title: "IMLeader Interface"
project: ""
interface: "IMLeader"
member: ""
kind: "interface"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMLeader.html"
---

# IMLeader Interface

Allows access to an MLeader.

## Syntax

### Visual Basic

```vb
Public Interface IMLeader
```

### C#

```csharp
public interface IMLeader
```

### JScript

```
public interface IMLeader
```

### Managed Extensions for C++

```
public __gc __interface IMLeader
```

### C++/CLI

```cpp
public interface class IMLeader
```

## Examples

C# code snippet:

public override void Execute()
{
CommandMessage commandline = application.GetCommandMessage();
if (null == commandline)
{
return;
}

Document dsDoc = application.GetActiveDocument();
if (null == dsDoc)
{
return;
}

Model dsModel = dsDoc.GetModel();
if (null == dsModel)
{
return;
}

SketchManager dsSketchManager = dsModel.GetSketchManager();
if (null == dsSketchManager)
{
return;
}

MLeader dsMLeader = dsSketchManager.**InsertMLeaderWithNoneContentType**( new double[] { 0.0, 0.0, 0.0, 100.0, 100.0, 0.0 }, dsMLeaderType_e.dsMLeaderType_Straight);
if (null == dsMLeader)
{
commandline.PrintLine("InsertMLeaderWithNoneContentType: Failed to create MLeader");
}

dsMLeader = dsSketchManager.**InsertMLeaderWithToleranceContentType**(new double[] { 0.0, 0.0, 0.0, 150.0, 150.0, 0.0 }, "{\\Fgdt;i}vvvb{\\Fgdt;l}vv\n5\n123", dsMLeaderType_e.dsMLeaderType_Straight, dsMLeaderTolAttachmentType_e.dsMLeaderTolAttachmentType_Middle );
if (null == dsMLeader)
{
commandline.PrintLine("InsertMLeaderWithToleranceContentType: Failed to create MLeader");
}

// Please create a block for this method
dsMLeader = dsSketchManager.**InsertMLeaderWithBlockContentType**(new double[] { 0.0, 0.0, 0.0, 200.0, 200.0, 0.0 }, "<block name>", dsMLeaderType_e.dsMLeaderType_Straight);
if (null == dsMLeader)
{
commandline.PrintLine("InsertMLeaderWithBlockContentType: Failed to create MLeader");
}

dsMLeader = dsSketchManager.**InsertMLeaderWithNoteContentType**(new double[] { 0.0, 0.0, 0.0, 250.0, 250.0, 0.0 }, 20.0, "MLeader with note", dsMLeaderType_e.dsMLeaderType_Straight);
if (null == dsMLeader)
{
commandline.PrintLine("InsertMLeaderWithNoteContentType: Failed to create MLeader");
}
}

## Remarks

For more information about MultiLeaders, see these **DraftSight user-interface help > Creating and Modifying Dimensions > Working With Leaders and Geometric Tolerances** topics:

- Creating MultiLeaders
- Modifying MultiLeaders
- Working with MultiLeaderStyles

## Accessors

[IDocument::GetObjectByHandle](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetObjectByHandle.html)

[ISelectionManager::GetSelectedObject](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObject.html)

[ISelectionManager::GetSelectedObjects](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObjects.html)

[ISketchManager::GetEntities](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~GetEntities.html)

[ISketchManager::InsertMLeaderWithBlockContentType](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertMLeaderWithBlockContentType.html)

[ISketchManager::InsertMLeaderWithNoneContentType](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertMLeaderWithNoneContentType.html)

[ISketchManager::InsertMLeaderWithNoteContentType](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertMLeaderWithNoteContentType.html)

[ISketchManager::InsertMLeaderWithToleranceContentType](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertMLeaderWithToleranceContentType.html)

## Access Diagram

[MLeader](DSObjectModel.pdf#MLeader)

## See Also

[IMLeader Members](Interop.dsAutomation~Interop.dsAutomation.IMLeader_members.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[ILeader Interface](Interop.dsAutomation~Interop.dsAutomation.ILeader.html)
