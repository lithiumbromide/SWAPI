---
title: "Partition Rollback and API Handles"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/Partition_Rollback_and_API_Handles.htm"
---

# Partition Rollback and API Handles

Partition rollback, introduced in SOLIDWORKS 2003, has changed the way that SOLIDWORKS caches bodies.

| Before partition rollback: | The FeatureManager design tree and bodies were cached. Cached bodies remained valid even if a model was rolled back to a state where one or more bodies had not yet been created, because the SOLIDWORKS API was able to get hold of the cached bodies. |
| --- | --- |
| With the introduction of partition rollback: | Bodies are no longer cached. Thus, the SOLIDWORKS API handle is not valid after a model is rolled back to a state where one or more bodies have not yet been created. |
