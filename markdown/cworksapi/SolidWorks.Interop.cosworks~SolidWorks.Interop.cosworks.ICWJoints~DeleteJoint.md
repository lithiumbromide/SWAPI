---
title: "DeleteJoint Method (ICWJoints)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWJoints"
member: "DeleteJoint"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWJoints~DeleteJoint.html"
---

# DeleteJoint Method (ICWJoints)

Deletes the specified joint.

## Syntax

### Visual Basic (Declaration)

```vb
Sub DeleteJoint( _
   ByVal Disp As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWJoints
Dim Disp As System.Object

instance.DeleteJoint(Disp)
```

### C#

```csharp
void DeleteJoint(
   System.object Disp
)
```

### C++/CLI

```cpp
void DeleteJoint(
   System.Object^ Disp
)
```

### Parameters

- `Disp`: Joint to delete

## VBA Syntax

See [CWJoints::DeleteJoint](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWJoints~DeleteJoint.html).

## Remarks

To delete a joint:

1. [Begin editing](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWJoints~JointsBeginEdit.html).
2. Delete a joint by calling this method.
3. [Save your modification](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWJoints~IncludeKeepModifiedJointOnUpdate.html).
4. [Calculate](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWJoints~CalculateJoints.html) the joints.
5. [End editing](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWJoints~JointsEndEdit.html).

## See Also

[ICWJoints Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWJoints.html)
[ICWJoints Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWJoints_members.html)

## Availability

SOLIDWORKS Simulation API 2010 SP0
