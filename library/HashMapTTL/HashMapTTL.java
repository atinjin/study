package com.atinjin;

import static java.util.Collections.*;

import java.util.Collection;
import java.util.HashMap;
import java.util.Map;
import java.util.Set;
import java.util.concurrent.TimeUnit;

public class HashMapTTL<K, V> implements Map<K, V> {

	private final HashMap<K, V> hashMap = new HashMap<>();
	private final HashMap<K, Long> timestampMap = new HashMap<>();
	private final long ttl;

	public HashMapTTL(TimeUnit ttlUnit, long ttlValue) {
		this.ttl = ttlUnit.toNanos(ttlValue);
	}

	@Override
	public V get(Object key) {
		V value = this.hashMap.get(key);
		if (Objects.nonNull(value) && expired(key, value)) {
			hashMap.remove(key);
			timestampMap.remove(key);
			return null;
		}

		return value;
	}

	private boolean expired(Object key) {
		Long nanoSecond = timestampMap.get(key);
		return Objects.isNull(nanoSecond) || (System.nanoTime() - timestampMap.get(key)) > this.ttl;
	}

	@Override
	public V put(K key, V value) {
		timestampMap.put(key, System.nanoTime());
		return hashMap.put(key, value);
	}

	@Override
	public int size() {
		clearExpired();
		return hashMap.size();
	}

	@Override
	public boolean isEmpty() {
		clearExpired();
		return hashMap.isEmpty();
	}

	@Override
	public boolean containsKey(Object key) {
		clearExpired();
		return hashMap.containsKey(key);
	}

	@Override
	public boolean containsValue(Object value) {
		clearExpired();
		return hashMap.containsValue(value);
	}

	@Override
	public V remove(Object key) {
		timestampMap.remove(key);
		return hashMap.remove(key);
	}

	@Override
	public void putAll(Map<? extends K, ? extends V> m) {
		for (Map.Entry<? extends K, ? extends V> e : m.entrySet()) {
			this.put(e.getKey(), e.getValue());
		}
	}

	@Override
	public void clear() {
		timestampMap.clear();
		hashMap.clear();
	}

	@Override
	public Set<K> keySet() {
		clearExpired();
		return unmodifiableSet(hashMap.keySet());
	}

	@Override
	public Collection<V> values() {
		clearExpired();
		return unmodifiableCollection(hashMap.values());
	}

	@Override
	public Set<java.util.Map.Entry<K, V>> entrySet() {
		clearExpired();
		return unmodifiableSet(hashMap.entrySet());
	}

	private void clearExpired() {
		for (K key : hashMap.keySet()) {
			if (expired(key)) {
				hashMap.remove(key);
				timestampMap.remove(key);
			}
		}
	}

}